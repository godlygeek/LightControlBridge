from http_server_manager import HttpServerManager
from http_request_manager import HttpRequestManager
from dns_request_manager import DnsRequestManager
from event_executor import EventExecutor
from uart_manager import UartManager
from params import Params

import gc
import os
import traceback


def main():
	executor = EventExecutor()

	uart_manager = UartManager()
	params = Params(uart_manager)
	HttpServerManager(params).register(executor)
	DnsRequestManager().register(executor)
	uart_manager.register(executor)
	executor.handle_events()


def main_wrapper():
	while True:
		try:
			main()
		except Exception as exc:
			gc.collect()
			if not os.path.exists('err.log'):
				with open('err.log', 'w') as errlog:
					traceback.print_exc(file=errlog)

main_wrapper()

# vim: set ts=4 sw=4 noet:
