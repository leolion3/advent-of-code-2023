<main>
<article class="day-desc"><h2>--- Day 7: Camel Cards ---</h2><p>Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an <a href="https://en.wikipedia.org/wiki/Airship" target="_blank">airship</a>. (At least it's a <span title="Please only read this sentence while listening to 'The Airship Blackjack' from the Final Fantasy 6 soundtrack."><em>cool</em> airship</span>!) It drops you off at the edge of a vast desert and descends back to Island Island.</p>
<p>"Did you bring the parts?"</p>
<p>You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large <a href="https://en.wikipedia.org/wiki/Dromedary" target="_blank">camel</a>.</p>
<p>"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.</p>
<p>"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.</p>
<p>After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the <em>parts</em> they need to fix the machines.</p>
<p>You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.</p>
<p>Because the journey will take a few days, she offers to teach you the game of <em>Camel Cards</em>. Camel Cards is sort of similar to <a href="https://en.wikipedia.org/wiki/List_of_poker_hands" target="_blank">poker</a> except it's designed to be easier to play while riding a camel.</p>
<p>In Camel Cards, you get a list of <em>hands</em>, and your goal is to order them based on the <em>strength</em> of each hand. A hand consists of <em>five cards</em> labeled one of <code>A</code>, <code>K</code>, <code>Q</code>, <code>J</code>, <code>T</code>, <code>9</code>, <code>8</code>, <code>7</code>, <code>6</code>, <code>5</code>, <code>4</code>, <code>3</code>, or <code>2</code>. The relative strength of each card follows this order, where <code>A</code> is the highest and <code>2</code> is the lowest.</p>
<p>Every hand is exactly one <em>type</em>. From strongest to weakest, they are:</p>
<ul>
<li><em>Five of a kind</em>, where all five cards have the same label: <code>AAAAA</code></li>
<li><em>Four of a kind</em>, where four cards have the same label and one card has a different label: <code>AA8AA</code></li>
<li><em>Full house</em>, where three cards have the same label, and the remaining two cards share a different label: <code>23332</code></li>
<li><em>Three of a kind</em>, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: <code>TTT98</code></li>
<li><em>Two pair</em>, where two cards share one label, two other cards share a second label, and the remaining card has a third label: <code>23432</code></li>
<li><em>One pair</em>, where two cards share one label, and the other three cards have a different label from the pair and each other: <code>A23A4</code></li>
<li><em>High card</em>, where all cards' labels are distinct: <code>23456</code></li>
</ul>
<p>Hands are primarily ordered based on type; for example, every <em>full house</em> is stronger than any <em>three of a kind</em>.</p>
<p>If two hands have the same type, a second ordering rule takes effect. Start by comparing the <em>first card in each hand</em>. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the <em>same label</em>, however, then move on to considering the <em>second card in each hand</em>. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.</p>
<p>So, <code>33332</code> and <code>2AAAA</code> are both <em>four of a kind</em> hands, but <code>33332</code> is stronger because its first card is stronger. Similarly, <code>77888</code> and <code>77788</code> are both a <em>full house</em>, but <code>77888</code> is stronger because its third card is stronger (and both hands have the same first and second card).</p>
<p>To play Camel Cards, you are given a list of hands and their corresponding <em>bid</em> (your puzzle input). For example:</p>
<pre><code>32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
</code></pre>
<p>This example shows five hands; each hand is followed by its <em>bid</em> amount. Each hand wins an amount equal to its bid multiplied by its <em>rank</em>, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.</p>
<p>So, the first step is to put the hands in order of strength:</p>
<ul>
<li><code>32T3K</code> is the only <em>one pair</em> and the other hands are all a stronger type, so it gets rank <em>1</em>.</li>
<li><code>KK677</code> and <code>KTJJT</code> are both <em>two pair</em>. Their first cards both have the same label, but the second card of <code>KK677</code> is stronger (<code>K</code> vs <code>T</code>), so <code>KTJJT</code> gets rank <em>2</em> and <code>KK677</code> gets rank <em>3</em>.</li>
<li><code>T55J5</code> and <code>QQQJA</code> are both <em>three of a kind</em>. <code>QQQJA</code> has a stronger first card, so it gets rank <em>5</em> and <code>T55J5</code> gets rank <em>4</em>.</li>
</ul>
<p>Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (<code>765</code> * 1 + <code>220</code> * 2 + <code>28</code> * 3 + <code>684</code> * 4 + <code>483</code> * 5). So the <em>total winnings</em> in this example are <code><em>6440</em></code>.</p>
<p>Find the rank of every hand in your set. <em>What are the total winnings?</em></p>
</article>
<p>Your puzzle answer was <code>253205868</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>To make things a little more interesting, the Elf introduces one additional rule. Now, <code>J</code> cards are <a href="https://en.wikipedia.org/wiki/Joker_(playing_card)" target="_blank">jokers</a> - wildcards that can act like whatever card would make the hand the strongest type possible.</p>
<p>To balance this, <em><code>J</code> cards are now the weakest</em> individual cards, weaker even than <code>2</code>. The other cards stay in the same order: <code>A</code>, <code>K</code>, <code>Q</code>, <code>T</code>, <code>9</code>, <code>8</code>, <code>7</code>, <code>6</code>, <code>5</code>, <code>4</code>, <code>3</code>, <code>2</code>, <code>J</code>.</p>
<p><code>J</code> cards can pretend to be whatever card is best for the purpose of determining hand type; for example, <code>QJJQ2</code> is now considered <em>four of a kind</em>. However, for the purpose of breaking ties between two hands of the same type, <code>J</code> is always treated as <code>J</code>, not the card it's pretending to be: <code>JKKK2</code> is weaker than <code>QQQQ2</code> because <code>J</code> is weaker than <code>Q</code>.</p>
<p>Now, the above example goes very differently:</p>
<pre><code>32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
</code></pre>
<ul>
<li><code>32T3K</code> is still the only <em>one pair</em>; it doesn't contain any jokers, so its strength doesn't increase.</li>
<li><code>KK677</code> is now the only <em>two pair</em>, making it the second-weakest hand.</li>
<li><code>T55J5</code>, <code>KTJJT</code>, and <code>QQQJA</code> are now all <em>four of a kind</em>! <code>T55J5</code> gets rank 3, <code>QQQJA</code> gets rank 4, and <code>KTJJT</code> gets rank 5.</li>
</ul>
<p>With the new joker rule, the total winnings in this example are <code><em>5905</em></code>.</p>
<p>Using the new joker rule, find the rank of every hand in your set. <em>What are the new total winnings?</em></p>
</article>
<p>Your puzzle answer was <code>253907829</code>.</p>
</main>