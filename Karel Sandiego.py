EMOJIS = {
    'locations': {
        'Windhoek': '🇳🇦',  # Namibia
        'Dubai': '🇦🇪',  # UAE
        'Caracas': '🇻🇪',  # Venezuela
        'Santiago de Chile': '🇨🇱',  # Chile
        'Montevideo': '🇺🇾',  # Uruguay
        'Kiev': '🇺🇦'  # Ukraine
    },
    'people': {
        'Dan': '👨',
        'Chris Piech': '👨🏫',
        'Grimace': '👹',
        'Rahul': '👦',
        'Franko': '🕵️',
        'Ramon': '👴',
        'Rodrigo': '👱'
    },
    'actions': {
        'success': '✅',
        'error': '❌',
        'warning': '⚠️',
        'info': 'ℹ️',
        'location': '📍',
        'connections': '🔗',
        'people': '👥',
        'clue': '🔍',
        'treasure': '🏆',
        'locked': '🔒',
        'unlocked': '🔓',
        'hidden': '👁',
        'visible': '✨',
        'karel': '🦹',
        'center': '🏬'
    }
}

game = {
    "locations": {
        "Windhoek": {"connections": ["Dubai", "Caracas"], "starts-locked": False, "karel": False},
        "Dubai": {"connections": ["Caracas", "Montevideo", "Santiago de Chile"], "starts-locked": True, "karel": False},
        "Kiev": {"connections": ["Santiago de Chile"], "starts-locked": True, "karel": False},
        "Santiago de Chile": {"connections": ["Dubai", "Montevideo", "Kiev"], "starts-locked": True, "karel": True},
        "Caracas": {"connections": ["Dubai", "Windhoek"], "starts-locked": True, "karel": False},
        "Montevideo": {"connections": ["Dubai"], "starts-locked": True, "karel": False}
    },
    "people": {
        "Franko": {"location": "Caracas",
                   "conversation": "I hear she may have ran off to Santiago de Chile. Try searching the Costanera Center.",
                   "starts-hidden": False, "unlock-locations": ["Santiago de Chile"], "unlock-people": [],
                   "unlock-clues": ["Costanera Center"]},
        "Grimace": {"location": "Dubai",
                    "conversation": "An investigator in Caracas named Franko has a clue for you.  ",
                    "starts-hidden": True, "unlock-locations": ["Caracas"], "unlock-people": ["Franko"],
                    "unlock-clues": []},
        "Dan": {"location": "Windhoek",
                "conversation": "Hi, your goal is to catch Karel, you need to talk to Chris Piech.  He's here in town.  ",
                "starts-hidden": False, "unlock-locations": [], "unlock-people": ["Chris Piech"], "unlock-clues": []},
        "Chris Piech": {"location": "Windhoek",
                        "conversation": "Grimace in Dubai has lost his diamonds, Karel stole them! You should go and talk to him there.  ",
                        "starts-hidden": True, "unlock-locations": ["Dubai"], "unlock-people": ["Grimace", "Rahul"],
                        "unlock-clues": []},
        "Ramon": {"location": "Montevideo",
                  "conversation": "She was here a while ago, I think she may have ran off back to Dubai.  ",
                  "starts-hidden": False, "unlock-locations": [], "unlock-people": [], "unlock-clues": []},
        "Rodrigo": {"location": "Santiago de Chile",
                    "conversation": "I saw her two days ago, you should search for her at the Costanera Center!",
                    "starts-hidden": True, "unlock-locations": [], "unlock-people": [], "unlock-clues": []},
        "Rahul": {"location": "Dubai",
                  "conversation": "I hear that Ramon in Montevideo has some information for you.  ",
                  "starts-hidden": True, "unlock-locations": ["Montevideo"], "unlock-people": ["Ramon"],
                  "unlock-clues": []}
    },
    "clues": {
        "Costanera Center": {"location": "Santiago de Chile",
                             "clue-text": "A note was left saying Karel is hiding at the top floor of Costanera Center in Santiago de Chile!",
                             "starts-hidden": True, "unlock-locations": [], "unlock-people": ["Rodrigo"],
                             "unlock-clues": []}
    },
    "current-location": "Windhoek"
}

game_locs = game['locations']
game_people = game['people']
game_clues = game['clues']


def print_header():
    """Print game header with ASCII art"""
    print("\n")
    print("╔════════════════════════════════════════════════╗")
    print("║    🕵️  WHERE IN THE WORLD IS KAREL SANDIEGO?  🕵️  ║")
    print("║         Stanford Code in Place 2026             ║")
    print("╚════════════════════════════════════════════════╝")
    print()


def print_location_map(current_location):
    """Print map showing current location"""
    print("\n" + "═" * 60)
    print("🗺️  YOUR CURRENT POSITION")
    print("═" * 60)

    emoji = EMOJIS['locations'].get(current_location, '📍')

    print(f"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║         YOU ARE HERE: {emoji} {current_location}                 ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    connections = game_locs[current_location]['connections']
    locked = game_locs[current_location]['starts-locked']

    print(f"🔗 Connected to: {', '.join(connections)}")
    if locked:
        print(f"🔒 This location is LOCKED (you arrived here)")
    else:
        print(f"🔓 This location is UNLOCKED")

    print("═" * 60 + "\n")


def print_person_card(person_name, conversation):
    """Print a decorative card for a person with highlighted dialogue"""
    emoji = EMOJIS['people'].get(person_name, '👤')

    print("\n" + "═" * 60)
    print(f"  {emoji}  ═══ PERSON CARD: {person_name} ═══")
    print("═" * 60)
    print(f"  👤 Location: {game_people[person_name]['location']}")
    print(f"  📊 Status: {EMOJIS['actions']['visible']} Visible")
    print("═" * 60)

    # Highlighted dialogue box
    print("\n  🗣️  ═══ 💬 DIALOGUE 💬 ═══")
    print("  ╔───────────────────────────────────────────────╗")
    print(f"  ║  {conversation}")
    print("  ╚───────────────────────────────────────────────╝")
    print("  🗣️  ════════════════════════════════════════════")
    print()


def print_clue_card(clue_name, clue_text):
    """Print a decorative card for a clue with highlighted text"""
    print("\n" + "═" * 60)
    print(f"  🔍  ═══ CLUE CARD: {clue_name} ═══")
    print("═" * 60)
    print(f"  📍 Location: {game_clues[clue_name]['location']}")
    print(f"  📊 Status: {EMOJIS['actions']['visible']} Discovered")
    print("═" * 60)

    # Highlighted clue text box
    print("\n  📜  ═══ 🔎 CLUE TEXT 🔎 ═══")
    print("  ╔───────────────────────────────────────────────╗")
    print(f"  ║  {clue_text}")
    print("  ╚───────────────────────────────────────────────╝")
    print("  📜  ════════════════════════════════════════════")
    print()


def print_progress():
    """Print game progress summary in one horizontal line"""
    spoken_count = len(spoken_to)
    total_people = len(game_people)
    clues_found = sum(1 for clue in game_clues if not game_clues[clue]['starts-hidden'])
    total_clues = len(game_clues)
    unlocked = sum(1 for loc in game_locs if not game_locs[loc]['starts-locked'])
    total_locs = len(game_locs)

    print(f"\n{'═' * 70}")
    print(
        f"  📊 GAME PROGRESS: 👥 {spoken_count}/{total_people}  │  🔍 {clues_found}/{total_clues}  │  📍 {unlocked}/{total_locs}  │  🎯 {search_count}/3")
    print(f"{'═' * 70}\n")


def can_go(locations, start, destination):
    visited = {}
    for place in locations:
        visited[place] = False
    return can_go_rec(locations, start, destination, visited)


def can_go_rec(locations, start, destination, visited):
    if start == destination:
        return True

    visited[start] = True

    for next_loc in locations[start]['connections']:
        if not visited[next_loc] and not locations[next_loc]['starts-locked']:
            if can_go_rec(locations, next_loc, destination, visited):
                return True

    return False


def talk_to(locations, people, clues, person, current_location):
    if person not in people:
        print(f"\n{EMOJIS['actions']['error']} This person does not exist (check spelling)\n")
        return False

    if people[person]['location'] != current_location:
        print(f"\n{EMOJIS['actions']['error']} {person} is not at this location\n")
        return False

    if people[person]['starts-hidden']:
        print(f"\n{EMOJIS['actions']['error']} {person} is hidden and cannot be talked to yet\n")
        return False

    print_person_card(person, people[person]['conversation'])
    people[person]['starts-hidden'] = False

    for unlocked_loc in people[person]['unlock-locations']:
        locations[unlocked_loc]['starts-locked'] = False
    for unlocked_person in people[person]['unlock-people']:
        people[unlocked_person]['starts-hidden'] = False
    for unlocked_clue in people[person]['unlock-clues']:
        clues[unlocked_clue]['starts-hidden'] = False

    return True


def investigate_clue(current_loc, locations, people, clues):
    clue_found = None
    for clue_name, clue_data in clues.items():
        if clue_data['location'] == current_loc and not clue_data['starts-hidden']:
            clue_found = clue_name
            break

    if clue_found is None:
        for clue_name, clue_data in clues.items():
            if clue_data['location'] == current_loc:
                print(f"\n{EMOJIS['actions']['info']} There is a clue here but you haven't discovered it yet\n")
                return
        print(f"\n{EMOJIS['actions']['error']} No such clue found at this location\n")
        return

    print_clue_card(clue_found, clues[clue_found]['clue-text'])
    clues[clue_found]['starts-hidden'] = False

    for unlocked_loc in clues[clue_found]['unlock-locations']:
        locations[unlocked_loc]['starts-locked'] = False
    for unlocked_person in clues[clue_found]['unlock-people']:
        people[unlocked_person]['starts-hidden'] = False
    for unlocked_clue in clues[clue_found]['unlock-clues']:
        clues[unlocked_clue]['starts-hidden'] = False


def is_karel_here(current_loc, locations):
    return locations[current_loc]['karel'] == True


def display_menu():
    """Display the main menu horizontally in 2 lines"""
    print("\n" + "═" * 70)
    print("  🎮 MAIN MENU - CHOOSE YOUR ACTION")
    print("═" * 70)
    print("  1. 👥 View people  │  2. 📍 View locations  │  3. 🔍 View clues")
    print("  4. 🛫 Travel        │  5. 💬 Talk to person  │  6. 🔎 Investigate")
    print("  7. 🏆 Catch Karel   │  8. 🚪 Exit game")
    print("═" * 70 + "\n")


def display_people(current_location):
    """Display available people at current location"""
    print("\n" + "─" * 50)
    print(f"  👥 PEOPLE IN {current_location}:")
    print("─" * 50)

    available = []
    for person in game_people:
        if game_people[person]['location'] == current_location:
            available.append(person)

    if not available:
        print(f"\n  {EMOJIS['actions']['info']} No people available at this location.\n")
        return []

    for i, person in enumerate(available, 1):
        emoji = EMOJIS['people'].get(person, '👤')
        if game_people[person]['starts-hidden']:
            status = f"{EMOJIS['actions']['hidden']} Hidden"
        else:
            status = f"{EMOJIS['actions']['warning']} Not spoken" if person not in spoken_to else f"{EMOJIS['actions']['success']} Spoken"
        print(f"  {i}.  {emoji} {person} {status}")

    print()
    return available


def display_locations():
    """Display available locations"""
    print("\n" + "─" * 50)
    print("  📍 AVAILABLE LOCATIONS:")
    print("─" * 50)

    available = []
    for loc in game_locs:
        if game_locs[loc]['starts-locked'] == False:
            available.append(loc)

    for i, loc in enumerate(available, 1):
        emoji = EMOJIS['locations'].get(loc, '📍')
        karel_here = game_locs[loc]['karel']
        karel_emoji = f" {EMOJIS['actions']['karel']} KAREL!" if karel_here else ""
        print(f"  {i}.  {emoji} {loc}{karel_emoji}")

    print()
    return available


def display_clues():
    """Display discovered clues"""
    print("\n" + "─" * 50)
    print("  🔍 DISCOVERED CLUES:")
    print("─" * 50)

    available = []
    for clue in game_clues:
        if game_clues[clue]['starts-hidden'] == False:
            available.append(clue)

    if not available:
        print(f"\n  {EMOJIS['actions']['info']} You haven't discovered any clues yet.\n")
        return []

    for i, clue in enumerate(available, 1):
        print(f"  {i}.  🔎 {clue}")

    print()
    return available


def get_travel_option():
    """Display travel options and get user selection"""
    print("\n" + "─" * 50)
    print("  🛫 TRAVEL - CONNECTED LOCATIONS:")
    print("─" * 50)

    current = game['current-location']
    available = game_locs[current]['connections']

    print(f"\n  📍 Current: {current}")
    print(f"  🔗 Connections: {', '.join(available)}")
    print()

    for i, loc in enumerate(available, 1):
        emoji = EMOJIS['locations'].get(loc, '📍')
        locked = game_locs[loc]['starts-locked']
        karel_here = game_locs[loc]['karel']
        karel_emoji = f" {EMOJIS['actions']['karel']} KAREL!" if karel_here else ""
        status = f"{EMOJIS['actions']['locked']} Locked" if locked else f"{EMOJIS['actions']['unlocked']} Available"
        print(f"  {i}.  {emoji} {loc} {status}{karel_emoji}")

    print()
    return available


def get_person_option(current_location):
    """Display person options and get user selection"""
    print("\n" + "─" * 50)
    print("  💬 TALK TO - PEOPLE AT YOUR LOCATION:")
    print("─" * 50)

    available = []
    for person in game_people:
        if game_people[person]['location'] == current_location and not game_people[person]['starts-hidden']:
            available.append(person)

    if not available:
        print(f"\n  {EMOJIS['actions']['info']} No people available to talk to at this location.\n")
        return []

    for i, person in enumerate(available, 1):
        emoji = EMOJIS['people'].get(person, '👤')
        if person not in spoken_to:
            status = f"{EMOJIS['actions']['warning']} Not spoken"
        else:
            status = f"{EMOJIS['actions']['success']} Spoken"
        print(f"  {i}.  {emoji} {person} {status}")

    print()
    return available


def print_location_info():
    """Print current location information"""
    current = game['current-location']
    emoji = EMOJIS['locations'].get(current, '📍')
    karel_here = game_locs[current]['karel']
    karel_banner = f"\n  {EMOJIS['actions']['karel']} ⚠️  KAREL SANDIEGO MIGHT BE HERE! ⚠️ {EMOJIS['actions']['karel']}" if karel_here else ""

    print(f"\n╔══════════════════════════════════════════════════╗")
    print(f"║  {emoji}  CURRENT LOCATION: {current}                 ║")
    print(f"╚══════════════════════════════════════════════════╝")
    if karel_banner:
        print(karel_banner)
    print(f"  🔗 Connections: {', '.join(game_locs[current]['connections'])}")

    if current == "Santiago de Chile":
        print(f"  🏬 🏢 SPECIAL: Costanera Center is here! 🔍")
    print()


def print_game_over(victory):
    """Print game over screen with ASCII art"""
    print("\n")
    if victory:
        print("╔════════════════════════════════════════════════╗")
        print("║         🎉 🏆 VICTORY! 🏆 🎉                    ║")
        print("║                                                ║")
        print("║   YOU HAVE CAUGHT KAREL SANDIEGO!              ║")
        print("║   YOU WIN THE GAME!                            ║")
        print("║                                                ║")
        print("║   🦹 → 👮 YOU WIN THE GAME! 👮 → 🦹            ║")
        print("║                                                ║")
        print("║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           ║")
        print("║   🌟🌟🌟 CONGRATULATIONS! 🌟🌟🌟               ║")
        print("╚════════════════════════════════════════════════╝")
    else:
        print("╔════════════════════════════════════════════════╗")
        print("║         ❌ 💔 GAME OVER 💔 ❌                    ║")
        print("║                                                ║")
        print("║   YOU COULDN'T FIND KAREL SANDIEGO             ║")
        print("║   IN 3 SEARCHES!                               ║")
        print("║                                                ║")
        print("║   🦹 → 😢 YOU LOSE THE GAME! 😢 → 🦹           ║")
        print("║                                                ║")
        print("║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           ║")
        print("║   😔 TRY AGAIN! 😔                               ║")
        print("╚════════════════════════════════════════════════╝")
    print("\n")


if __name__ == '__main__':
    global spoken_to
    global search_count
    spoken_to = []
    search_count = 0
    karel_found = False
    game_over = False

    # Print game header ONLY ONCE at the beginning
    print_header()

    while not game_over:
        print_location_info()
        display_menu()

        try:
            choice = input("  🎯 Select an option (1-8): ").strip()
        except:
            print(f"\n{EMOJIS['actions']['error']} Invalid input\n")
            continue

        if choice == '1':
            available = display_people(game['current-location'])
            if available:
                try:
                    person_choice = input("  💬 Who do you want to talk to? (enter number or 0 to exit): ").strip()
                    if person_choice == '0':
                        continue
                    person_idx = int(person_choice)
                    if 1 <= person_idx <= len(available):
                        person = available[person_idx - 1]
                        if talk_to(game_locs, game_people, game_clues, person, game['current-location']):
                            spoken_to.append(person)
                            print(f"\n{EMOJIS['actions']['success']} You talked to {person}\n")
                        else:
                            print(f"\n{EMOJIS['actions']['error']} You couldn't talk to that person\n")
                    else:
                        print(f"\n{EMOJIS['actions']['error']} Invalid number\n")
                except ValueError:
                    print(f"\n{EMOJIS['actions']['error']} Invalid input\n")
            else:
                print(f"\n{EMOJIS['actions']['info']} No people available\n")

        elif choice == '2':
            available = display_locations()
            if available:
                print(f"\n{EMOJIS['actions']['info']} To travel, use option 4 and select a connected location.\n")

        elif choice == '3':
            available = display_clues()
            if available:
                print(
                    f"\n{EMOJIS['actions']['info']} To investigate, use option 6 if you're in the correct location.\n")

        elif choice == '4':
            available = get_travel_option()
            if available:
                try:
                    travel_choice = input("  🛫 Where do you want to travel? (enter number): ").strip()
                    travel_idx = int(travel_choice)
                    if 1 <= travel_idx <= len(available):
                        destination = available[travel_idx - 1]
                        if game_locs[destination]['starts-locked']:
                            print(
                                f"\n{EMOJIS['actions']['error']} {destination} is locked. You need to find a clue or talk to someone to unlock it.\n")
                        elif can_go(game_locs, game['current-location'], destination):
                            game['current-location'] = destination
                            if destination == "Santiago de Chile":
                                print(
                                    f"\n{EMOJIS['actions']['success']} You have travelled to {destination}! {EMOJIS['actions']['karel']} Karel might be nearby!\n")
                            else:
                                print(f"\n{EMOJIS['actions']['success']} You have travelled to {destination}!\n")

                            print_location_map(destination)
                        else:
                            print(f"\n{EMOJIS['actions']['error']} There is no unlocked path to {destination}\n")
                    else:
                        print(f"\n{EMOJIS['actions']['error']} Invalid number\n")
                except ValueError:
                    print(f"\n{EMOJIS['actions']['error']} Invalid input\n")
            else:
                print(f"\n{EMOJIS['actions']['info']} No locations available\n")

        elif choice == '5':
            available = get_person_option(game['current-location'])
            if available:
                try:
                    talk_choice = input("  💬 Who do you want to talk to? (enter number): ").strip()
                    talk_idx = int(talk_choice)
                    if 1 <= talk_idx <= len(available):
                        person = available[talk_idx - 1]
                        if person not in spoken_to:
                            if talk_to(game_locs, game_people, game_clues, person, game['current-location']):
                                spoken_to.append(person)
                                print(f"\n{EMOJIS['actions']['success']} You talked to {person}\n")
                        else:
                            print(f"\n{EMOJIS['actions']['warning']} You already talked to {person}\n")
                    else:
                        print(f"\n{EMOJIS['actions']['error']} Invalid number\n")
                except ValueError:
                    print(f"\n{EMOJIS['actions']['error']} Invalid input\n")
            else:
                print(f"\n{EMOJIS['actions']['info']} No people available to talk to\n")

        elif choice == '6':
            print("\n" + "─" * 50)
            print("  🔎 INVESTIGATE CLUE:")
            print("─" * 50)
            print(f"\n  📍 You are at: {game['current-location']}")

            has_discoverable_clue = False
            for clue_name, clue_data in game_clues.items():
                if clue_data['location'] == game['current-location']:
                    has_discoverable_clue = True
                    if clue_data['starts-hidden']:
                        print(f"\n  {EMOJIS['actions']['clue']} There is a clue here: {clue_name} (undiscovered)")
                    else:
                        print(f"\n  {EMOJIS['actions']['clue']} Discovered clue: {clue_name}")

            if has_discoverable_clue:
                investigate_clue(game['current-location'], game_locs, game_people, game_clues)
                print(f"{EMOJIS['actions']['success']} Clue investigated\n")
            else:
                print(f"\n{EMOJIS['actions']['error']} No clues at this location\n")

        elif choice == '7':
            print("\n" + "═" * 60)
            print(
                f"  {EMOJIS['actions']['karel']} 🏆 {EMOJIS['actions']['karel']} CATCH KAREL {EMOJIS['actions']['karel']} 🏆 {EMOJIS['actions']['karel']}")
            print("═" * 60)
            print(f"\n  📍 You are at: {game['current-location']}")

            if game['current-location'] != "Santiago de Chile":
                print(f"\n  {EMOJIS['actions']['error']} You must be in the right location to catch Karel!\n")
            else:
                print(f"\n  🎯 Searches used: {search_count}/3")
                print()

                confirm = input("  🏆 Do you want to try to catch Karel? (1=Yes, 2=No): ").strip()
                if confirm == '1':
                    karel_found = is_karel_here(game['current-location'], game_locs)
                    if karel_found:
                        game_over = True
                        karel_found = True
                        search_count += 1
                        print(f"\n{EMOJIS['actions']['success']} KAREL FOUND!\n")
                    elif not karel_found and search_count >= 3:
                        game_over = True
                        print(f"\n{EMOJIS['actions']['error']} Karel is not here and you have used all your searches\n")
                    else:
                        search_count += 1
                        print(f"\n{EMOJIS['actions']['error']} Karel is not here. Searches used: {search_count}/3\n")
                else:
                    print(f"\n{EMOJIS['actions']['warning']} You decided not to catch her now\n")

        elif choice == '8':
            print("\n" + "─" * 50)
            print("  🚪 EXIT THE GAME:")
            print("─" * 50)
            confirm = input("  1. Yes, exit\n  2. No, continue\n  Select (1-2): ").strip()
            if confirm == '1':
                game_over = True
                print(f'\n{EMOJIS["actions"]["success"]} You have exited the game\n')
            else:
                print(f"\n{EMOJIS['actions']['warning']} You will continue playing\n")

        else:
            print(f"\n{EMOJIS['actions']['error']} Invalid option. Select a number from 1 to 8\n")

        # Show progress in one horizontal line
        print_progress()

    # Print game over screen
    print_game_over(karel_found)

