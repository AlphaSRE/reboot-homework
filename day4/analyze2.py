完整版本
#!/usr/bin/env python
# coding=utf-8
http_dict = dict()
with open("/home/share/www_access_20140823.log",'r') as lines:
    for line in lines:
        line_list = line.split()
        http_code = line_list[8]
        http_url = line_list[6]
        http_ip = line_list[0]
        if http_code in http_dict:
            if http_url in http_dict[http_code]:
                http_dict[http_code][http_url][http_ip] = http_dict[http_code][http_url].get(http_ip, 0) + 1
            else:
                http_dict[http_code][http_url] = {http_ip:1}
        else:
            http_dict[http_code] = {http_url:{http_ip:1}}

    httpl = []
    for code,url in http_dict.iteritems():
        for url,ip_count in url.iteritems():
            for ip in ip_count.iteritems():
                httpl.append([code,url,ip])
    #print httpl
    for l in sorted(httpl, key=lambda x:x[2][1], reverse=True)[:10]:
        print l
