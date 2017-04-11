## 1、analyze.py ##
### 1、加载字典 ###
	jieba.load_userdict('resource/dict.txt')

dict.txt的内容：

	石宇 100 nr
	尚华 100 nr
	金常务 100 nr
	...

dict.txt的解释：  
第一个字段石宇是切割以后的分词  
第二个字段100是词频（设1的时候金常务还是会被切割成 金-常务）  
第三个字段nr是词性人名


### 2、加载剧本 ###
	bfile = codecs.open('resource/busan.txt', "r", "utf8")

得到文件对象bfile将来在while循环通过 line = bfile.readline() 获得每一行

### 3、lineNames数组 ###
	//每一行出现的名字
	//例如：
	//lineNames = [
		["石宇","尚华"],//第一行
		[],//第二行
		["金常务"],//第三行
	]

### 4、relationships对象 ###
	//保存每个角色和其他角色在同一句同时出现的次数
	{
		"美少女": {
			"珍熙": 1
		},
		"尚华": {
			"游弋": 1,
			"塞进": 1,
			"爱抚": 4,
			"珍熙": 1,
			"秀安": 12,
			"英国": 16,
			"卡住": 4,
			"呼唤": 1,
			"明白": 2,
			"石宇": 61,
			"露宿者": 4,
			"盛京": 45
		}
	}

### 5、生成lineNames ###
	while (True):
		//每次读取下一行
	    line = bfile.readline()
		
		//line是''代表剧本没有下一句了直接break
	    if (line == ''):
	        break
		//line是'\r\n'代表这一行是剧本的换行直接continue
	    elif (line == '\r\n'):
	        continue
		//剩下的情况才是真正的需要分析的剧本
	    else:
			//获得这一行的分词
	        wordArray = posseg.cut(line)
	
	        //每读一行就给lineNames加入一个空数组
	        lineNames.append([])

			//遍历这一行的分词 如果这个词是人名且长度大于等于2 就插入lineNames中最新的数组
	        for w in wordArray:
	            if (w.flag == 'nr' and len(w.word) >= 2):
	                lineNames[-1].append(w.word)

### 5、生成relationships ###
	for line in lineNames:
		//把这一行的所有名字两两比对 
	    for name1 in line:
	        for name2 in line:
				//两个名字相同说明是同一个人
	            if name1 == name2:
	                continue
				//流程到这一步说明是两个人
				//{"石宇"：{}}
	            if relationships.get(name1) is None:
	                relationships[name1] = {}
	
				//{"石宇"：{"尚华"：1}}
	            if relationships[name1].get(name2) is None:
	                relationships[name1][name2] = 1
				//{"石宇"：{"尚华"：2}}
	            else:
	                relationships[name1][name2] = relationships[name1][name2] + 1

### 6、打印relationships ###
	print json.dumps(relationships, ensure_ascii=False, encoding='UTF-8')



## 2、Gephi ##
### 1、下载Gephi ###
[http://www.121down.com/soft/softview-72193.html](http://www.121down.com/soft/softview-72193.html)
![](resource/Untitled.png)