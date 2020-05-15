"""
Use a stack to check whether or not a string has a balanced set of parantheses

Balanced = ({[]})
Not balanced = {]

"""
from stack import Stack


def isParenBalanced(parenString):
	s = Stack()
	index = 0
	is_balanced = True
	
	parenDict = {"(" : ")", "{" : "}", "[" : "]"}
		
	while is_balanced and index < len(parenString):
		current_paren = parenString[index]
		if current_paren in parenDict.values():
			#print(s.get_stack())
			if s.isEmpty() or parenDict[s.pop()] != current_paren:
				#if stack is empty and current is a closing paren
				#or current is not equal to open paren
				is_balanced = False
		else:
			#print(s.get_stack())
			s.push(current_paren)
		
		index+=1

	#print(s.get_stack())
	if not s.isEmpty():
		#stack should be empty at the end if balanced
		is_balanced = False

	return is_balanced
		
print("Is this balanced? '({[]})'", isParenBalanced("({[]})"))
print("Is this balanced? '({{}}'", isParenBalanced("({{}}"))

