import csv
import sys
import logging

from util import Node, StackFrontier, QueueFrontier

logging.basicConfig(level=logging.disable)


# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    queue_frontier = QueueFrontier()
    explored = set()
    path = []
    logging.info(f'Source actor is {people[source]["name"]} ({source}) and initial movies are {people[source]["movies"]}')

    # add initial node to the frontier
    # Node state = the actor
    # Node action = the movie
    queue_frontier.add(Node(state=source, parent=None, action=None))

    while True:
        
        if queue_frontier.empty():
            raise Exception('No Solution found')
        
        # Explore next node in the frontier
        current_node = queue_frontier.remove()
        logging.debug(f"current_node={current_node.state}")
        
        # For each connection (returned from neighbors_for_person function) 
        # create a node and add it to the frontier. Unless it is already in 
        # the frontier or it has been explored.
        for movie, person in neighbors_for_person(current_node.state):
            logging.debug(f'Movie:{movie}, Person:{person}')
            
            if not queue_frontier.contains_state(person) and person not in explored:

                # Check if the current node is the target person
                if person == target:
                    logging.info(f"Connection found between {source} and {target}")
                    
                    # Add the last node to the path without creating a Node object
                    path = [(movie, person)]

                    # Create the path going to the initial node
                    while current_node.parent is not None:
                        path.insert(0, (current_node.action, current_node.state))       
                        current_node = current_node.parent
                    return path

                queue_frontier.add(Node(state=person, parent=current_node, action=movie))

        # Add to the explored set
        explored.add(current_node.state) 

    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
