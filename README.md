<h1>Duplicate Question Detector</h1>

This project is focused on finding duplicate questions on stackoverflow.com website.
It has 2 main components; the text and code comparator.
Text comparison is performed using GloVe implementation; which basically accepts text corpus and returns context-based word vectors.
Code comparison has 2 approaches:
  i) Using MD5-Hashing on tokens parsed from code blocks and comparing it with another by applying a similarity function.
  ii) Using Longest Common Subsequence (LCS) on tokens values obtained from the code snippets.
  
The final result will be the mean of the text and code comparator scores.

<h2>Constraints:</h2>
Current focus is on 'C' language tagged questions.
