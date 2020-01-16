class Evaluator:
	@staticmethod
	def zip_evaluate(words, coefs):
		if len(words) != len(coefs):
			print(-1)
			return
		res_lst = [len(x) * y for x, y in zip(words, coefs)]
		res = sum(res_lst)
		print(res)
	
	@staticmethod
	def enumerate_evaluate(words, coefs):
		if len(words) != len(coefs):
			print(-1)
			return
		res_lst = []
		for i, (v1, v2) in enumerate(zip(words, coefs)):
			res_lst.append(len(v1) * v2)
		res = sum(res_lst)
		print(res)

Evaluator.zip_evaluate(["Le", "Lorem", "Ipsum", "est", "simple"], [1.0, 2.0, 1.0, 4.0, 0.5])
