"""
Develop a Knowledge based agent capable of making informed decisions within a 
specific environment
"""
"""
Knowledge based Agent that can provide information about few C programming 
    complie/run behaviors, errors, causes, and solutions
    
Map few C program compile run behavior to known causes and solutions
"""
"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

            Figure 7.1  A generic knowledge-based agent
    Given a percept, the agent adds the percept to its knowledge base
    Asks the knowledge base for the best action, and 
    Tells the knowledge base that it has in fact taken that action
    
        function KB-AGENT( percept ) returns an action
        
            persistent: KB , a knowledge base
            t , a counter, initially 0, indicating time
        
            TELL (KB, MAKE-PERCEPT-SENTENCE(percept, t))            
            action ← ASK (KB, MAKE-ACTION-QUERY(t))            
            TELL (KB, MAKE-ACTION-SENTENCE(action, t ))            
            t ← t + 1            
            return action
"""
"""
Knowledge Base, list of dictionaries, errors and behavior:
        Behavior, what happens when the error occurs
        Error Type, name of error        
        Causes, possible reasons for the error
        Solutions, recommended fixes for the error
"""
knowledge_base = [
    {"behavior": "Compilation fails with error messages indicating syntax issues",  
     "error_type": "Syntax Error", 
     "causes": ["missing semicolon", "mismatched parentheses", 
                "incorrect use of keywords"], 
     "solutions": ["Review code for missing punctuation", 
                   "Ensure all parentheses and brackets are properly matched", 
                   "Consult language documentation for correct syntax"]},
    {"behavior": "Program crashes or throws exception when division by zero", 
     "error_type": "Runtime Error: Division by Zero", 
     "causes": ["attempting to divide a number by zero"], 
     "solutions": ["Check for zero before performing division", 
                   "Implement error handling to manage division operations"]},
    {"behavior": "Program crashes or terminates unexpectedly", 
     "error_type": "Segmentation Fault",       
     "causes": ["dereferencing null pointer", "uninitialized pointer", 
                "accessing out-of-bounds array index"],
     "solutions": ["Ensure pointers are initialized before use", 
                   "Check array indices to prevent out-of-bounds access", 
                   "Trace pointer values"]},
    {"behavior": "Program runs but produces incorrect results", 
     "error_type": "Logic Error", 
     "causes": ["incorrect algorithm implementation", "off-by-one errors", 
                "wrong conditional statements"], 
     "solutions": ["Review algorithm logic and flow", 
                   "Use print statements to trace variable values", 
                   "Test edge cases to identify logical flaws" ]}]
"""
Agent , Behavior (init, ask)
"""    
class KnowledgeBaseAgent:   # class encapsulates the functionality of the agent
    
    def __init__(self, knowledge_base):  # Initialize agent with knowledge base
        self.knowledge_base = knowledge_base        

    def ask(self, behavior):     # Returns kb with most matching behavior words
                
        behavior_words = behavior.lower().split()  # for case-insensitive match
        word_match_count_kb_entry = []    # save [(word match count, kb entry)]
        
        for entry in self.knowledge_base:
            matches = []           # Save behavior word match in knowledge base
            kb_beh_err = entry['behavior'] + " " + entry['error_type']
            
            for word in behavior_words:                # For all behavior words
                                                      
                if word in kb_beh_err.lower():  # case insensitive match
                    matches.append(word)
            
            if matches:     # If any matches of behavior word in knowledge base
                word_match_count_kb_entry.append((len(matches), entry))

        if word_match_count_kb_entry:      # return kb with most matching words
            word_match_count_kb_entry.sort(key=lambda x: x[0], reverse=True)
            return word_match_count_kb_entry[0][1]
        else: 
            return "Behavior not found" #else return message behavior not found


agent = KnowledgeBaseAgent(knowledge_base) # Create KnowledgeBaseAgent instance

behavior = input(" Enter behavior/results of compilation/program run: ")

info = agent.ask(behavior)     # retrieve error information from Knowledge Base 

if info == "Behavior not found":
    print(f"\n {behavior}: {info} in Knowledge Base")
else:    
    print(f"\n Behavior: {info['behavior']}")    
    print(f"\n Error Type: {info['error_type']}")    
    print(f"\n Likely causes: \n\t {',\n\t '.join(info['causes'])}")
    print(f"\n Possible fixes / solutions: \n\t {',\n\t '.join(info['solutions'])}")

    
"""
Output:

 Enter behavior/results of compilation/program run: Compilation with syntax error

 Behavior: Compilation fails with error messages indicating syntax issues

 Error Type: Syntax Error

 Likely causes: 
	 missing semicolon,
	 mismatched parentheses,
	 incorrect use of keywords

 Possible fixes / solutions: 
	 Review code for missing punctuation,
	 Ensure all parentheses and brackets are properly matched,
	 Consult language documentation for correct syntax
"""    

"""
Output:

 Enter behavior/results of compilation/program run: Undefined reference

 Undefined reference: Behavior not found in Knowledge Base
"""
