import sqlite3
con = sqlite3.connect("youtube.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("select * FROM videos")
    print("\n")
    print("*"*70)
    data = cursor.fetchall()
    for index, name , time in data:
        print(f"{index}. Name: {name}, Duration: {time}")
    print("*"*70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)" , (name, time))
    con.commit()

def update_video(video_id, name, time):
    list_all_videos()
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name , time, video_id))
    con.commit()

def delete_video(video_id):
    list_all_videos()
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the program")
        choice = input("Enter your choice\n")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name\n")
                time = input("Enter the video time\n")
                add_video(name , time)
            case '3':
                video_id = input("Enter video id to update\n")
                name = input("Enter the video name\n")
                time = input("Enter the video time\n")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter video id to delete\n")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice please enter a valid choice")
    con.close()

if __name__ == "__main__":
    main()
