class pyColor:
	green = "\033[32m"
	blue = "\033[1;34m"
	yellow = "\033[1;33m"
	cyan = "\033[36m"
	lcyan = "\033[1;36m"
	reset = "\033[0m"
	
	def proc(self,text):
		return(self.green+"[*]"+self.reset+text)
	def result(self,text):
		return(self.lcyan+text+self.reset)