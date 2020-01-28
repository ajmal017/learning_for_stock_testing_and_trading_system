"""
Event-driven framework of vn.py framework.
"""

from collections import defaultdict
from queue import Empty, Queue
from threading import Thread
from time import sleep
from typing import Any, Callable

EVENT_TIMER = "eTimer"
#这个有什么用呢
"""
调用start()方法，事件处理线程和计时器同时启动，计时器每隔一秒调用___run_timer()方法，
创建计时器事件，调用put()方法在队尾插入一个事件，事件处理线程每隔一秒获取事件，
若存在事件调用__process()方法，对事件进行处理。
"""

class Event:
    """
    Event object consists of a type string which is used
    by event engine for distributing event, and a data
    object which contains the real data.
    """

    def __init__(self, type: str, data: Any = None):
        """"""
        self.type = type
        self.data = data


# Defines handler function to be used in event engine.
HandlerType = Callable[[Event], None]


class EventEngine:
    """
    Event engine distributes event object based on its type
    to those handlers registered.

    It also generates timer event by every interval seconds,
    which can be used for timing purpose.
    """

    def __init__(self, interval: int = 1):
        """
        Timer event is generated every 1 second by default, if
        interval not specified.
        """
        self._interval = interval
        self._queue = Queue()#队列，FIFO，有put和get方法
        self._active = False
        self._thread = Thread(target=self._run)#线程中工作的函数是self._run
        self._timer = Thread(target=self._run_timer)#此处表示线程工作中运行的是self._run_timer
        self._handlers = defaultdict(list)#defaultdic可以在访问字典中不存在的键时，不会返回错误
        self._general_handlers = []

    def _run(self):
        """
        Get event from queue and then process it.
        如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用；
        如果队列为空且block为False，队列将引发Empty异常。
        """
        while self._active:
            try:
                event = self._queue.get(block=True, timeout=1)
                self._process(event)
            except Empty:
                pass

    def _process(self, event: Event):
        """
        First ditribute event to those handlers registered listening
        to this type.

        Then distrubute event to those general handlers which listens
        to all types.

        优先检查是否存在对该事件进行监听的处理函数，然后调用通用处理函数进行处理
        计时器启动
        """
        if event.type in self._handlers:
            [handler(event) for handler in self._handlers[event.type]]
        #如果此handler在self._handlers中，就用handler对应的函数处理event
        if self._general_handlers:
            [handler(event) for handler in self._general_handlers]

    def _run_timer(self):
        """
        Sleep by interval second(s) and then generate a timer event.
        """
        while self._active:
            sleep(self._interval)
            event = Event(EVENT_TIMER)
            self.put(event)

    def start(self):
        """
        Start event engine to process events and generate timer events.
        利用thread把self.timer和_run_timer联系起来，每隔1000秒这个线程会被调用
        """
        self._active = True
        self._thread.start()
        self._timer.start()

    def stop(self):
        """
        Stop event engine.
        """
        self._active = False
        self._timer.join()
        self._thread.join()

    def put(self, event: Event):
        """
        Put an event object into event queue.
        """
        self._queue.put(event)

    def register(self, type: str, handler: HandlerType):
        """
        Register a new handler function for a specific event type. Every
        function can only be registered once for each event type.
        """
        handler_list = self._handlers[type]
        if handler not in handler_list:
            handler_list.append(handler)

    def unregister(self, type: str, handler: HandlerType):
        """
        Unregister an existing handler function from event engine.
        """
        handler_list = self._handlers[type]

        if handler in handler_list:
            handler_list.remove(handler)

        if not handler_list:
            self._handlers.pop(type)

    def register_general(self, handler: HandlerType):
        """
        Register a new handler function for all event types. Every
        function can only be registered once for each event type.
        """
        if handler not in self._general_handlers:
            self._general_handlers.append(handler)

    def unregister_general(self, handler: HandlerType):
        """
        Unregister an existing general handler function.
        """
        if handler in self._general_handlers:
            self._general_handlers.remove(handler)
