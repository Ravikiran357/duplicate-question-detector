import os
import re

def replaceith(string, sub, wanted, n):
    position_of_sub = [m.start() for m in re.finditer(sub, string)][n]
    before = string[:position_of_sub]
    after = string[position_of_sub:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

def get_keyword_hash():
	f = open(('c_token_values.txt'),'r')
	key_val = f.read()
	key_val = key_val.split('@@')
	token_val_dict = {}
	for kv in key_val:
		if kv:
			token_val_dict[kv.split(':-')[0]] = kv.split(':-')[1]
	return token_val_dict

def get_program_tokens():
	f = open(('results/' + file_name),'r')
	tokens = f.read()
	token_count = tokens.count('##') - 1
	token_list = tokens.split('##')
	# for i in range(0, token_count):
	# 	if token_list[i + 1] == '(':
	# 		if re.match("^[A-Za-z]", token_list[i]):
	# 			#replace ith occurence of ##
	# 			tokens = replaceith(tokens, '##', '@#@##', i)
	# 			pass
	f.close()
	return token_list

file_names = os.listdir("results")
if not file_names:
	print("No files found")
	exit()
else:
	#n = input('Enter value for n\n')
	#k = input('Enter value for k\n')
	n = 4
	k = 3
	for file_name in file_names:
		if file_name.endswith(".tokens"):
			token_val_dict = get_keyword_hash()
			token_keys = token_val_dict.keys()
			tokens = get_program_tokens()
			n_gram_list = []
			n_gram_dict = {}
			new_functions_dict = {}
			new_functions_val = 200		
			for i in range(0,len(tokens)-1):
				token = tokens[i]
				if len(n_gram_list) == n:
					n_gram_code = ':'.join(n_gram_list)
					if n_gram_code in n_gram_dict.keys():
						n_gram_dict[n_gram_code] += 1
					else:
						n_gram_dict[n_gram_code] = 1
					n_gram_list = []

				if token in token_keys:
					n_gram_list.append(token_val_dict[token])
				else:
					#if '@#@' in token:
					# Looking for function names here
					if tokens[i + 1] == '(':
						token = token.replace('@#@', '')
						if token not in new_functions_dict.keys():
							new_functions_dict[token] = str(new_functions_val)
							new_functions_val += 1
						n_gram_list.append(new_functions_dict[token])
					else:
					# int-val,str-val,float-val, id (variable)
						n_gram_list.append('100')

			if len(n_gram_list) == n:
				n_gram_code = ':'.join(n_gram_list)
				if n_gram_code in n_gram_dict.keys():
					n_gram_dict[n_gram_code] += 1
				else:
					n_gram_dict[n_gram_code] = 1

			k_items_list = sorted(n_gram_dict, key=n_gram_dict.get)[0:3]
			print('FINALLY:')
			print(k_items_list)
			n_gram_list = n_gram_dict.keys()


			#try to convert to LCS problem


			score = 0
			query_seq = '64:100:85:100'
			query_seq = ':'.split(query_seq)
			for seq in query_seq:
				for item in n_gram_list:
					if seq in item:
						score += 1

			score /= len(n_gram_list)

# 			