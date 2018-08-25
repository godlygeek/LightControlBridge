import select


class EventExecutor:
	def __init__(self):
		self._handlers = {}
		self._poll = select.poll()

	def register(self, obj, on_readable, on_writable, on_hup, on_err):
		handlers = self._handlers.setdefault(obj.fileno(), {})
		mask = (select.POLLIN if on_readable else 0) | (
		        select.POLLOUT if on_writable else 0)
		handlers['on_readable'] = on_readable
		handlers['on_writable'] = on_writable
		handlers['on_hup'] = on_hup
		handlers['on_err'] = on_err
		self._poll.register(obj, mask)

	def unregister(self, obj):
		self._poll.unregister(obj)
		del self._handlers[obj.fileno()]

	def handle_events(self, timeout_ms=500):
		while True:
			for fd, events in self._poll.poll(timeout_ms):
				handlers = self._handlers[fd]
				if events & select.POLLERR:
					handlers['on_err']()
				elif events & select.POLLHUP:
					handlers['on_hup']()
				else:
					if events & select.POLLIN:
						handlers['on_readable']()
					if events & select.POLLOUT:
						handlers['on_writable']()

# vim: set ts=4 sw=4 noet:
