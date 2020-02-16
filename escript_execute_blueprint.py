#script
htmlcode = """
@@{ANSIBLE_HTML_CODE}@@
"""
htmlStringify = htmlcode.replace("\n", "\\n")

url = '@@{ANSIBLE_SERVER}@@/api/v2/job_templates/10/launch/'
username = '@@{CRED_AWX.username}@@'
password = '@@{CRED_AWX.secret}@@'
headers = {'Content-Type': 'application/json',  'Accept':'application/json'}
payload = {
    "extra_vars": "{\n \"html\": \"" + htmlStringify[2:] + "\"\n}",
    "limit": "@@{address}@@"
}

r = urlreq(url, auth='BASIC', verb='POST', user=username, passwd=password, params=json.dumps(payload), headers=headers, verify=False)

if r.ok:
    resp = json.loads(r.content)
    print resp
    exit(0)
else:
    print 'Post request failed', r.content
    exit(1)
