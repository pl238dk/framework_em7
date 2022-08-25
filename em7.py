import time
import json
import requests
# python3 -m pip install requests[socks]
requests.packages.urllib3.disable_warnings()

class EM7(object):
	def __init__(self, hostname):
		self.load_credentials(hostname)
		self.session = requests.Session()
		self.hostname = hostname
		self.base_url = f'https://{hostname}'
		# To configure a SOCKS5 proxy, if necessary
        #proxies = {
		#	'http': 'socks5h://127.0.0.1:1080',
		#	'https': 'socks5h://127.0.0.1:1080',
		#}
		#self.session.proxies = proxies
		headers = {
			'Accept': 'application/json',
		}
		self.session.headers.update(headers)
		return
	
	def load_credentials(self, hostname):
		'''
			keys = ['username','password']
		'''
		try:
			open('configuration.json','r')
		except:
			print('[E] Credentials not found')
		
		with open('configuration.json','r') as f:
			file_raw = f.read()
		credentials = json.loads(file_raw)
		self.un = credentials['credentials'][hostname]['username']
		self.pw = credentials['credentials'][hostname]['password']
		return
	
	##
	## Basic HTTP Handling
	
	def get(self, path, params={}):
		#url = f'{self.base_url}/api/{path}'
		url = f'{self.base_url}{path}'
		
		_params = {}
		for param_key in params:
			_params[param_key] = params[param_key]
		
		response = self.session.get(
			url,
			params=_params,
			auth=(self.un, self.pw),
			verify=False,
		)
		output = {
			'success': False,
			'result': response.text,
			'response': response,
		}
		if response.status_code == 200:
			output['success'] = True
			try:
				response_json = json.loads(
					response.text
				)
				output['result'] = response_json
			except:
				print('could not load JSON')
				pass
		return output
	
	def post(self, path, body={}, params={}):
		#url = f'{self.base_url}/api/{path}'
		url = f'{self.base_url}{path}'
		
		_params = {}
		for param_key in params:
			_params[param_key] = params[param_key]
		
		response = self.session.post(
			url,
			jason=body,
			params=_params,
			auth=(self.un, self.pw),
			verify=False,
		)
		output = {
			'success': False,
			'result': response.text,
			'response': response,
		}
		if response.status_code == 200:
			output['success'] = True
			try:
				response_json = json.loads(
					response.text
				)
				output['result'] = response_json
			except:
				print('could not load JSON')
				pass
		return output
	
	def put(self, path, body={}, params={}):
		#url = f'{self.base_url}/api/{path}'
		url = f'{self.base_url}{path}'
		
		_params = {}
		for param_key in params:
			_params[param_key] = params[param_key]
		
		response = self.session.put(
			url,
			jason=body,
			params=_params,
			auth=(self.un, self.pw),
			verify=False,
		)
		output = {
			'success': False,
			'result': response.text,
			'response': response,
		}
		if response.status_code == 200:
			output['success'] = True
			try:
				response_json = json.loads(
					response.text
				)
				output['result'] = response_json
			except:
				print('could not load JSON')
				pass
		return output
	
	def delete(self, path, params={}):
		#url = f'{self.base_url}/api/{path}'
		url = f'{self.base_url}{path}'
		
		_params = {}
		for param_key in params:
			_params[param_key] = params[param_key]
		
		response = self.session.delete(
			url,
			params=_params,
			auth=(self.un, self.pw),
			verify=False,
		)
		output = {
			'success': False,
			'result': response.text,
			'response': response,
		}
		if response.status_code == 200:
			output['success'] = True
			try:
				response_json = json.loads(
					response.text
				)
				output['result'] = response_json
			except:
				print('could not load JSON')
				pass
		return output
	
	##
	## API Functions
	
	def feature_list(self):
		output = self.get('/api')
		return output

	def get_access_lock(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/access_lock', params=_params)
		return output
	
	def get_account(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/account', params=_params)
		return output
	
	def get_account_policy(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/account_policy', params=_params)
		return output
	
	def get_alert(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/alert', params=_params)
		return output
	
	def get_asset(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/asset', params=_params)
		return output
	
	def get_cleared_event(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/cleared_event', params=_params)
		return output
	
	def get_contacts(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/contacts', params=_params)
		return output
	
	def get_credential(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/credential', params=_params)
		return output
	
	def get_dashboard(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/dashboard', params=_params)
		return output
	
	def get_data_performance(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/data_performance', params=_params)
		return output
	
	def get_data_performance_raw(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/data_performance_raw', params=_params)
		return output
	
	def get_device(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/device', params=_params)
		return output
	
	def get_device_group(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/device_group', params=_params)
		return output
	
	def get_discovery_session(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/discovery_session', params=_params)
		return output
	
	def get_discovery_session_active(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/discovery_session_active', params=_params)
		return output
	
	def get_dynamic_app(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/dynamic_app', params=_params)
		return output
	
	def get_event(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/event', params=_params)
		return output
	
	def get_filestore(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/filestore', params=_params)
		return output
	
	def get_interface_metric(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/interface_metric', params=_params)
		return output
	
	def get_monitor(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/monitor', params=_params)
		return output
	
	def get_organization(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/organization', params=_params)
		return output
	
	def get_relationship(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/relationship', params=_params)
		return output
	
	def get_relationship_hierarchy(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/relationship_hierarchy', params=_params)
		return output
	
	def get_schedule(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/schedule', params=_params)
		return output
	
	def get_system_threshold(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/system_threshold', params=_params)
		return output
	
	def get_task(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/task', params=_params)
		return output
	
	def get_threshold_value_override(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/threshold_value_override', params=_params)
		return output
	
	def get_ticket(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/ticket', params=_params)
		return output
	
	def get_ticket_category(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/ticket_category', params=_params)
		return output
	
	def get_ticket_chargeback(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/ticket_chargeback', params=_params)
		return output
	
	def get_ticket_log(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/ticket_log', params=_params)
		return output
	
	def get_ticket_note(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/ticket_note', params=_params)
		return output
	
	def get_vendor(self, limit=9999999):
		_params = {
			'limit': limit,
		}
		output = self.get('/api/vendor', params=_params)
		return output
			
	def _():
		return

if __name__ == '__main__':
	host = 'em7.domain.com'
	e = EM7(host)
	
	fl = e.feature_list()
	
	#f = fl['result'][1]['URI']
	#r = e.get(f)
	#accounts = [x for x in r['result']['result_set']]
	#for acc in accounts: print(acc['description'])
	
	'''
	# Write functions for functions
	for f in fl['result']:
		feature_name = f['URI'].split('/')[2]
		msg = (
			f'def get_{feature_name}(self, limit=9999999):\n'
			f'\t_params = {{\n'
			f'\t\t\'limit\': limit,\n'
			f'\t}}\n'
			f'\toutput = self.get(\'{f["URI"]}\', params=_params)\n'
			f'\treturn output\n\n'
		)
		print(msg)
	#'''
	
	'''
	# pull all assets, Pool
	d = e.get_asset()
	dd = [x['description'] for x in d['result']['result_set']]
	from multiprocessing.dummy import Pool
	p = Pool(64)
	results = p.map(e.get_asset, dd)
	#'''
	print('[I] End')