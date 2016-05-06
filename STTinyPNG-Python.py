import tinify
import os
import os.path

tinify.key = "RkoczqavMW1TjFrlhFE9WakzGCYmc2Rh" # AppKey
fromFilePath = "/Users/zpy/Desktop/test1" # 源路径
toFilePath = "/Users/zpy/Desktop/test2" # 输出路径

for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg':
			toFullPath = toFilePath + root[len(fromFilePath):]
			toFullName = toFullPath + '/' + name

			if os.path.isdir(toFullPath):
				pass
			else:
				os.mkdir(toFullPath)

			source = tinify.from_file(root + '/' + name)
			source.to_file(toFullName)
			
			with open(toFullName, 'rb') as source:
			    source_data = source.read()
			    result_data = tinify.from_buffer(source_data).to_buffer()
