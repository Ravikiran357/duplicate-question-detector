<h1>Duplicate Question Detector</h1>

This project is focused on finding duplicate questions on stackoverflow.com website. Current focus is on 'C' language tagged questions.
It has 2 main components; the text and code comparator.<br>
Text comparison is performed using GloVe implementation; which basically accepts text corpus and returns context-based word vectors.
Code comparison has 2 approaches:
  i) Using MD5-Hashing on tokens parsed from code blocks and comparing it with another by applying a similarity function.
  ii) Using Longest Common Subsequence (LCS) on tokens values obtained from the code snippets.
  
The final result will be the mean of the text and code comparator scores.

<h3>Pre-requisite</h3>
1. Requires Python 3.5 to run.<br>


<h3>Usage</h3>
Generate the code token values:<br>
<code>python c_parser.py -c add_num.c -t</code><br>
<code>python c_parser.py -c add_num2.c -t</code>

Run the code comparator:<br>
<code>python c_token_evaluator</code>
