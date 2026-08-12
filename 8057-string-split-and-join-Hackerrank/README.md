# [String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true)
## Easy
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>In Python, a string can be split on a delimiter.  </p>

<p><strong>Example:</strong>  </p>

<pre><code>&gt;&gt;&gt; a = "this is a string"
&gt;&gt;&gt; a = a.split(" ") # a is converted to a list of strings. 
&gt;&gt;&gt; print a
['this', 'is', 'a', 'string']
</code></pre>

<p>Joining a string is simple:  </p>

<pre><code>&gt;&gt;&gt; a = "-".join(a)
&gt;&gt;&gt; print a
this-is-a-string 
</code></pre>

<p><strong>Task</strong> <br>
You are given a string. Split the string on a <code>" "</code> (space) delimiter and join using a <code>-</code> hyphen.   </p>

<p><strong>Function Description</strong>   </p>

<p>Complete the <em>split_and_join</em> function in the editor below.   </p>

<p><em>split_and_join</em> has the following parameters:   </p>

<ul>
<li><em>string line:</em> a string of space-separated words   </li>
</ul>

<p><strong>Returns</strong>   </p>

<ul>
<li><em>string:</em> the resulting string   </li>
</ul>

<p><strong>Input Format</strong> <br>
The one line contains a string consisting of space separated words.  </p>

<p><strong>Sample Input</strong> </p>

<pre><code>this is a string   
</code></pre>

<p><strong>Sample Output</strong>  </p>

<pre><code>this-is-a-string
</code></pre></div></div></div></div>