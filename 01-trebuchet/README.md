<main>
<article class="day-desc"><h2>--- Day 1: Trebuchet?! ---</h2><p>Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.</p>
<p>You've been doing this long enough to know that to restore snow operations, you need to check all <em class="star">fifty stars</em> by December 25th.</p>
<p>Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <em class="star">one star</em>. Good luck!</p>
<p>You try to ask why they can't just use a <a href="/2015/day/1">weather machine</a> ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") <span title="My hope is that this abomination of a run-on sentence somehow conveys the chaos of being hastily loaded into a trebuchet.">and</span> hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a <a href="https://en.wikipedia.org/wiki/Trebuchet" target="_blank">trebuchet</a> ("please hold still, we need to strap you in").</p>
<p>As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been <em>amended</em> by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.</p>
<p>The newly-improved calibration document consists of lines of text; each line originally contained a specific <em>calibration value</em> that the Elves now need to recover. On each line, the calibration value can be found by combining the <em>first digit</em> and the <em>last digit</em> (in that order) to form a single <em>two-digit number</em>.</p>
<p>For example:</p>
<pre><code>1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
</code></pre>
<p>In this example, the calibration values of these four lines are <code>12</code>, <code>38</code>, <code>15</code>, and <code>77</code>. Adding these together produces <code><em>142</em></code>.</p>
<p>Consider your entire calibration document. <em>What is the sum of all of the calibration values?</em></p>
</article>
<p>Your puzzle answer was <code>54450</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Your calculation isn't quite right. It looks like some of the digits are actually <em>spelled out with letters</em>: <code>one</code>, <code>two</code>, <code>three</code>, <code>four</code>, <code>five</code>, <code>six</code>, <code>seven</code>, <code>eight</code>, and <code>nine</code> <em>also</em> count as valid "digits".</p>
<p>Equipped with this new information, you now need to find the real first and last digit on each line. For example:</p>
<pre><code>two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
</code></pre>
<p>In this example, the calibration values are <code>29</code>, <code>83</code>, <code>13</code>, <code>24</code>, <code>42</code>, <code>14</code>, and <code>76</code>. Adding these together produces <code><em>281</em></code>.</p>
<p><em>What is the sum of all of the calibration values?</em></p>
</article>
<p>Your puzzle answer was <code>54265</code>.</p>
</main>
