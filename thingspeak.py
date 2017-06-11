import urllib
import urllib2

THINGSPEAKKEY = '<<REDACTED>>'
THINGSPEAKURL = 'https://api.thingspeak.com/update'

#order is important!
def sendData(*argv):
	values = {'api_key' : THINGSPEAKKEY}

	count = 1;
	for arg in argv:
		values['field'+str(count)] = arg;
		count += 1;


	postdata = urllib.urlencode(values)
	req = urllib2.Request(THINGSPEAKURL, postdata)


	try:
		# Send data to Thingspeak
		response = urllib2.urlopen(req, None, 5)
		html_string = response.read()
		response.close()
		print 'Update ' + html_string

	except urllib2.HTTPError, e:
		print 'Server could not fulfill the request. Error code: ' + e.code
	except urllib2.URLError, e:
		print 'Failed to reach server. Reason: ' + e.reason
	except:
		print 'Unknown error'

