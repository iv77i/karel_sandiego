# karel_sandiego
A python version of the 80's game "Where in the world is Carmen Sandiego?", as final project for Stanford Code in Place 2026


<h1>🎮 Where in the World is Karel Sandiego?</h1>
<h2 class="center">Game Cheat Sheet & Winning Guide</h2>

<p class="center"><strong>A Python-based adventure game where you track Karel Sandiego across 6 cities worldwide.</strong></p>

<hr>

<h2>📍 QUICK SUMMARY</h2>

<table>
    <tr>
        <th>Attribute</th>
        <th>Value</th>
    </tr>
    <tr>
        <td><strong>Objective</strong></td>
        <td>Find and capture <strong>Karel Sandiego</strong></td>
    </tr>
    <tr>
        <td><strong>Karel's Location</strong></td>
        <td>Santiago de Chile (Costanera Center)</td>
    </tr>
    <tr>
        <td><strong>Starting Location</strong></td>
        <td>Windhoek, Namibia</td>
    </tr>
    <tr>
        <td><strong>Search Limit</strong></td>
        <td>3 attempts to capture</td>
    </tr>
    <tr>
        <td><strong>Cities</strong></td>
        <td>6 total</td>
    </tr>
</table>

<hr>

<h2>🗺️ COMPLETE ROUTE TO WIN</h2>
<h3>Step-by-Step Guide</h3>

<h4>Step 1: Windhoek (Starting location)</h4>
<pre>
Actions:
  1. Talk to Dan → He tells you to search for Chris Piech
  2. Talk to Chris Piech → Dubai + Grimace + Rahul unlocked
</pre>

<h4>Step 2: Travel to Dubai</h4>
<pre>
Travel: Windhoek → Dubai

Actions in Dubai:
  1. Talk to Grimace 👧 → Caracas + Franko unlocked
  2. Talk to Rahul → Montevideo + Ramon unlocked
</pre>

<h4>Step 3: Travel to Caracas</h4>
<pre>
Travel: Dubai → Caracas

Actions in Caracas:
  1. Talk to Franko → Santiago de Chile + Clue "Costanera Center" unlocked
</pre>

<h4>Step 4: Travel to Santiago de Chile</h4>
<pre>
Travel: Caracas → Dubai → Santiago de Chile

Actions in Santiago de Chile:
  1. Talk to Rodrigo → Verifies Karel is here
  2. Investigate → Confirms the clue "Costanera Center"
</pre>

<h4>Step 5: CAPTURE KAREL! 🏆</h4>
<pre>
Menu → Option 7: "Catch Karel"
  → Confirm with "1"
  → VICTORY! 🏆
</pre>

<hr>

<h2>🔄 ROUTE SUMMARY TABLE</h2>

<table>
    <tr>
        <th>#</th>
        <th>Location</th>
        <th>Action</th>
        <th>Unlocks</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Windhoek 🇳🇦</td>
        <td>Talk to Dan 👨</td>
        <td>-</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Windhoek 🇳🇦</td>
        <td>Talk to Chris Piech 👨🏫</td>
        <td>Dubai, Grimace, Rahul</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Dubai 🇦🇪</td>
        <td>Travel from Windhoek</td>
        <td>-</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Dubai 🇦🇪</td>
        <td>Talk to Grimace 👧</td>
        <td>Caracas, Franko</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Dubai 🇦🇪</td>
        <td>Talk to Rahul 👦</td>
        <td>Montevideo, Ramon</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Caracas 🇻🇪</td>
        <td>Travel from Dubai</td>
        <td>-</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Caracas 🇻🇪</td>
        <td>Talk to Franko 🕵️</td>
        <td>Santiago de Chile, Costanera Center</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Dubai 🇦🇪</td>
        <td>Travel from Caracas</td>
        <td>-</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Santiago de Chile 🇨🇱</td>
        <td>Travel from Dubai</td>
        <td>-</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Santiago de Chile 🇨🇱</td>
        <td>Talk to Rodrigo 👱</td>
        <td>-</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Santiago de Chile 🇨🇱</td>
        <td>Option 7: Catch Karel</td>
        <td>🏆 YOU WIN!</td>
    </tr>
</table>

<hr>

<h2>🗺️ CONNECTION MAP</h2>

<pre>
        Windhoek (🇳🇦)
           /        \
          /          \
     Dubai (🇦🇪)  Caracas (🇻🇪)
      /   |   \        |
     /    |    \       |
Montevideo Santiago  (only connects with Dubai)
  (🇺🇾)    (🇨🇱)*
            \
             \
            Kiev (🇺🇦)

* = Where Karel is 🦹
</pre>

<h3>City Connections</h3>

<table>
    <tr>
        <th>City</th>
        <th>Country</th>
        <th>Connections</th>
        <th>Karel Here?</th>
    </tr>
    <tr>
        <td>Windhoek</td>
        <td>Namibia 🇳🇦</td>
        <td>Dubai, Caracas</td>
        <td>❌ No</td>
    </tr>
    <tr>
        <td>Dubai</td>
        <td>UAE 🇦🇪</td>
        <td>Caracas, Montevideo, Santiago, Windhoek</td>
        <td>❌ No</td>
    </tr>
    <tr>
        <td>Caracas</td>
        <td>Venezuela 🇻🇪</td>
        <td>Dubai, Windhoek</td>
        <td>❌ No</td>
    </tr>
    <tr>
        <td>Santiago de Chile</td>
        <td>Chile 🇨🇱</td>
        <td>Dubai, Montevideo, Kiev</td>
        <td class="highlight">✅ YES!</td>
    </tr>
    <tr>
        <td>Montevideo</td>
        <td>Uruguay 🇺🇾</td>
        <td>Dubai</td>
        <td>❌ No</td>
    </tr>
    <tr>
        <td>Kiev</td>
        <td>Ukraine 🇺🇦</td>
        <td>Santiago de Chile</td>
        <td>❌ No</td>
    </tr>
</table>

<hr>

<h2>⚡ CONTROL MENU</h2>

<pre>
1. View people      → See people at your location
2. View locations   → See unlocked locations
3. View clues       → See discovered clues
4. Travel           → Travel to another city
5. Talk to person   → Talk to someone
6. Investigate      → Investigate clue at your location
7. Catch Karel      → Try to capture! (only in Santiago)
8. Exit game        → Exit
</pre>

<hr>

<h2>🎯 FASTEST ROUTE (MINIMUM STEPS)</h2>

<pre>
Windhoek → Talk Dan → Talk Chris Piech → Dubai → 
Grimace → Caracas → Franko → Dubai → Santiago de Chile → 
Catch Karel → VICTORY! 🏆
</pre>

<p><strong>Statistics:</strong></p>
<ul>
    <li><strong>Total travels:</strong> 3 (Windhoek→Dubai, Dubai→Caracas, Dubai→Santiago)</li>
    <li><strong>Total conversations:</strong> 5 (Dan, Chris, Grimace, Rahul, Franko)</li>
    <li><strong>Total steps:</strong> 11 actions</li>
</ul>

<hr>

<h2>🚨 TROUBLESHOOTING</h2>
<h3>Common Problems</h3>

<table>
    <tr>
        <th>Problem</th>
        <th>Solution</th>
    </tr>
    <tr>
        <td>Can't travel to some city</td>
        <td>Talk to more people at your current location</td>
    </tr>
    <tr>
        <td>Can't find Karel</td>
        <td>She's only in <strong>Santiago de Chile</strong> - don't search elsewhere</td>
    </tr>
    <tr>
        <td>Searches run out</td>
        <td>Restart the game (Option 8 → Exit)</td>
    </tr>
    <tr>
        <td>Location is locked</td>
        <td>Find a clue or talk to someone to unlock it</td>
    </tr>
    <tr>
        <td>Person is hidden</td>
        <td>Unlock them by talking to the right person first</td>
    </tr>
</table>

<hr>

<h2>🎮 KEY RULES</h2>

<ul>
    <li>✅ You can <strong>only travel to connected and unlocked locations</strong></li>
    <li>✅ You must <strong>talk to people to unlock new cities</strong></li>
    <li>✅ Karel is in <strong>Santiago de Chile</strong> all the time</li>
    <li>✅ You have <strong>3 attempts to capture her</strong> (option 7)</li>
    <li>⚠️ If you <strong>fail 3 times, you lose the game</strong></li>
    <li>✅ You must be in <strong>Santiago de Chile</strong> to catch Karel</li>
</ul>

<hr>

<h2>👥 CHARACTERS</h2>

<table>
    <tr>
        <th>Person</th>
        <th>Emoji</th>
        <th>Location</th>
        <th>What They Unlock</th>
    </tr>
    <tr>
        <td>Dan</td>
        <td>👨</td>
        <td>Windhoek</td>
        <td>Chris Piech</td>
    </tr>
    <tr>
        <td>Chris Piech</td>
        <td>👨🏫</td>
        <td>Windhoek</td>
        <td>Dubai, Grimace, Rahul</td>
    </tr>
    <tr>
        <td>Grimace</td>
        <td>👧</td>
        <td>Dubai</td>
        <td>Caracas, Franko</td>
    </tr>
    <tr>
        <td>Rahul</td>
        <td>👦</td>
        <td>Dubai</td>
        <td>Montevideo, Ramon</td>
    </tr>
    <tr>
        <td>Franko</td>
        <td>🕵️</td>
        <td>Caracas</td>
        <td>Santiago de Chile, Costanera Center clue</td>
    </tr>
    <tr>
        <td>Ramon</td>
        <td>👴</td>
        <td>Montevideo</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Rodrigo</td>
        <td>👱</td>
        <td>Santiago de Chile</td>
        <td>-</td>
    </tr>
</table>

<hr>

<h2>🔍 CLUES</h2>
<h3>Costanera Center</h3>

<ul>
    <li><strong>Location:</strong> Santiago de Chile</li>
    <li><strong>Text:</strong> "A note was left saying Karel is hiding at the top floor of Costanera Center in Santiago de Chile!"</li>
    <li><strong>Unlocked by:</strong> Talking to Franko in Caracas</li>
    <li><strong>Unlocks:</strong> Rodrigo</li>
</ul>

<hr>

<h2 class="center">🏆 VICTORY SCREEN</h2>

<div class="center">
<pre>
╔════════════════════════════════════════════════╗
║         🎉 🏆 VICTORY! 🏆 🎉                    ║
║                                                ║
║   YOU HAVE CAUGHT KAREL SANDIEGO!              ║
║   YOU WIN THE GAME!                            ║
║                                                ║
║   🦹 → 👮 YOU WIN THE GAME! 👮 → 🦹            ║
║                                                ║
║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           ║
║   🌟🌟🌟 CONGRATULATIONS! 🌟🌟🌟               ║
╚════════════════════════════════════════════════╝
</pre>
</div>

<hr>

<h2 class="center">🎮 GAME OVER (LOSE)</h2>

<div class="center">
<pre>
╔════════════════════════════════════════════════╗
║         ❌ 💔 GAME OVER 💔 ❌                    ║
║                                                ║
║   YOU COULDN'T FIND KAREL SANDIEGO             ║
║   IN 3 SEARCHES!                               ║
║                                                ║
║   🦹 → 😢 YOU LOSE THE GAME! 😢 → 🦹           ║
║                                                ║
║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           ║
║   😔 TRY AGAIN! 😔                               ║
╚════════════════════════════════════════════════╝
</pre>
</div>

<hr>

<h2>📝 HOW TO RUN THE GAME</h2>

<ol>
    <li><strong>Install Python</strong> (if not already installed)</li>
    <li><strong>Download the game file</strong> (<code>carmen.py</code>)</li>
    <li><strong>Run the game:</strong> <code>python carmen.py</code></li>
    <li><strong>Follow the menu</strong> and use the cheat sheet above!</li>
</ol>

<hr>

<h2>🎯 QUICK WIN CHECKLIST</h2>

<pre>
[✓] Started at Windhoek
[✓] Talked to Dan
[✓] Talked to Chris Piech
[✓] Traveled to Dubai
[✓] Talked to Grimace 👧
[✓] Talked to Rahul
[✓] Traveled to Caracas
[✓] Talked to Franko
[✓] Traveled back to Dubai
[✓] Traveled to Santiago de Chile 🇨🇱
[✓] Talked to Rodrigo
[✓] Investigated Costanera Center
[✓] Used Option 7 to Catch Karel
[✓] VICTORY! 🏆
</pre>

<hr>

<h2>💡 PRO TIPS</h2>

<ol>
    <li><strong>Always check connections</strong> before traveling</li>
    <li><strong>Talk to everyone</strong> at each location</li>
    <li><strong>Investigate clues</strong> when you find them</li>
    <li><strong>Don't use Option 7</strong> until you're in Santiago de Chile</li>
    <li><strong>Save your searches</strong> - you only have 3!</li>
    <li><strong>Use the progress tracker</strong> (shown after each action) to monitor what you've unlocked</li>
</ol>

<hr>

<h2>🌟 VERSION INFO</h2>

<ul>
    <li><strong>Game:</strong> Where in the World is Karel Sandiego?</li>
    <li><strong>Platform:</strong> Python 3.x</li>
    <li><strong>Year:</strong> 2026</li>
    <li><strong>Event:</strong> Stanford Code in Place 2026</li>
</ul>

<hr>

<h2>📄 LICENSE</h2>
<p>This game is part of Stanford Code in Place 2026 curriculum.</p>

<hr>

<p class="center" style="font-size: 24px; color: #27ae60;">
<strong>Happy gaming! 🎮✨</strong>
</p>

<p class="center">
<em>Use this cheat sheet to win the game in under 15 minutes!</em>
</p>

</body>
</html>
