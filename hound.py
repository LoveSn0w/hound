# -*- coding:utf-8 -*-
import argparse,threading,time,function,random,dns.resolver
from table.tabulate import tabulate
from request.blast import blast; 
from  mysql.DB import DB;
from core import CORE
from crawler.crawler import crawler
parser = argparse.ArgumentParser()
parser.add_argument("-l",help=" -l  Update your dictionary "); #导入字典

parser.add_argument("-u",help=" -u  the website you want to request "); # 网站

parser.add_argument("-i",help=" -i  Call other interface query ");# 接口

parser.add_argument("-t",help=" -t  Set thread ",type=int );# 线程

parser.add_argument("--recursion",help=" --recursion   Recursive domain name   ");# 递归模式

parser.add_argument("--crawler" , help=" --crawler  Crawler thread", type=int);# 爬虫模式

#第一个参数是线程的 第二个参数是最大的网络爬虫

args = parser.parse_args() #最后通过parse_args()函数的解析

Dictionaries = args.l; #字典

url = args.u; #网站 

Interface = args.i;#接口



if args.t == None: #判断线程是否设置
	thread = 100;#线程
else:
	thread = args.t;#它设置的线程

recursion = args.recursion; #递归

h_crawler = args.crawler;#爬虫


picture = random.randint(1, 4); #生成随机数



tsk = [];  #等待线程结束的
crawler_progress = []; # 爬虫等待线程结束的

if thread > 500:
	print '\033[1;31;1m Command parse error ！！！ \033[0m';
	exit();

if __name__ == '__main__':
	hound_db = DB();
	blast = blast();
	if Dictionaries: #批量导入字典
		function.process(hound_db.Dictionaries,Dictionaries);
	elif url:
		if picture == 1:
			function.a1();
		elif picture == 2:
			function.a2();
		elif picture == 3:
			function.a3();
		elif picture == 4:
			function.a4();
		lis = hound_db.query_all("select lis from lis"); #获取所有字典数据
		
		print "\033[1;35;1m  Dictionary--> %i Tools--> hound version--> 1.0 \033[0m  \n" % (len(lis));

		url = url.replace('http://','').replace('https://',''); #处理域名
		sql = "select count(table_name) from information_schema.tables where table_name = '%s' and TABLE_SCHEMA = '%s'" % (url.replace('.','_'),CORE.db)
				
		if not DB().query(sql): #判断表名存不存在 如果不存在就创建
			DB().increase(""" 
				create table %s(
				id int not null primary key auto_increment,
				url text not null comment 'url',
				ip varchar(40)	not null comment 'ip',
				recursion int not null comment 'digui',
				Crawler int not null comment 'pachong'
				)charset utf8 engine = innodb;
			""" % (url.replace('.','_')) );
		try:
			u_resolver=dns.resolver.Resolver()
			ip = u_resolver.query(url,'A')
			if ip[0] :
				url_ip = ip[0];
		except Exception,e:
			url_ip = "0.0.0.0";
		sql = "insert into %s values(null,\"%s\",\"%s\",1,0)" % (url.replace('.','_'),url,url_ip);
		DB().increase(sql); #入库

		blast.blast_url(url,thread,lis); #爆破域名 并且等待结束

		if Interface == 'good': #如果调用接口
			'''调用接口查询'''
			from request.call_interface import call_interface;
			i_lis = call_interface.jiekou1(url); #获取接口输出的域名
			
			if len(i_lis) > 1:#如果获取到的域名超过一个的话
				
				from request.simple import simple;
				is_url = simple(); #new 对象
				print '\033[1;32;1m  Call interface to get the domain name...√  \033[0m';
				time.sleep(1);
				print '\033[1;32;1m  A total of %i domain names  \033[0m' % (len(i_lis));
				print '\033[1;32;1m  May consume a little time -_-  \033[0m'
				t1 = threading.Thread();
				t2 = threading.Thread();
				t3 = threading.Thread();
				t4 = threading.Thread();
				t5 = threading.Thread();
				t6 = threading.Thread();
				t7 = threading.Thread();
				t8 = threading.Thread();
				t9 = threading.Thread();
				t10 = threading.Thread();

				s = 0;

				while s < len(i_lis):
					
					if not t1.isAlive() and s < len(i_lis):
						t1 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t1.start();
						s = s+1;
					if not t2.isAlive() and s < len(i_lis):
						t2 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t2.start();
						s = s+1;
					if not t3.isAlive() and s < len(i_lis):
						t3 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t3.start();
						s = s+1;
					if not t4.isAlive() and s < len(i_lis):
						t4 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t4.start();
						s = s+1;
					if not t5.isAlive() and s < len(i_lis):
						t5 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t5.start();
						s = s+1;
					if not t6.isAlive() and s < len(i_lis):
						t6 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t6.start();
						s = s+1;
					if not t7.isAlive() and s < len(i_lis):
						t7 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t7.start();
						s = s+1;
					if not t8.isAlive() and s < len(i_lis):
						t8 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t8.start();
						s = s+1;
					if not t9.isAlive() and s < len(i_lis):
						t9 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t9.start();
						s = s+1;
					if not t10.isAlive() and s < len(i_lis):
						t10 = threading.Thread(target=is_url.h_get_isurl,args=[url,i_lis[s]]);
						t10.start();
						s = s+1;
					time.sleep(0.8);

	  			print '\033[1;32;1m This step is complete, the next to continue。\033[0m';
	  			'''接口调用完毕！'''
	  			time.sleep(2);   		
	  	
	  	function.table_print(url.replace('.','_')); #输出表格

	  	if recursion != None: #递归爆破
	  		time.sleep(3); 
			print ' Ready to burst, the need for a certain time! '
			while True:
				sql = "select url from %s where recursion = 0 limit 1" % (url.replace('.','_'));
				recursion_url = hound_db.query_all(sql);
				if len(recursion_url) > 0 :
			
					blast.recursion_blast_url(url,thread,lis,recursion_url); #查询1数据后进行爆破 并且等待爆破完2条
				else:
					break;
			
				time.sleep(1);
			print 'OK!'
			function.table_print(url.replace('.','_')); #输出表格


		if h_crawler != None:#爬虫
			while True:
				sql = "select url from %s where Crawler = 0 limit %i" % (url.replace('.','_') , h_crawler);
				crawler_url = hound_db.query_all(sql);
				if len(crawler_url) == 0 :
					break;

				for c_url in crawler_url:
					crawler_t = threading.Thread(target=crawler,args=[url.replace('.','_'),c_url[0]]);
					crawler_t.start();
					crawler_progress.append(crawler_t);
					sql = "update %s set Crawler = 1 where url = '%s'" % (url.replace('.','_'),c_url[0]); #爬虫完后 修改状态为已爬
					
					DB().increase(sql);
					time.sleep(2); 

				for tt in crawler_progress:
  					tt.join()
  					time.sleep(1); 
  			function.table_print(url.replace('.','_')); #输出表格




