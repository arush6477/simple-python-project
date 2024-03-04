from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<696969>:696969@youtubemanager.jv6iwns.mongodb.net/")

db = client['ytManager']
video_collection = db['videos']

def list_all_videos():
    print("\n")
    print("*"*70)
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Duration: {video['time']}")
    print("*"*70)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name":name, 'time':time}}
        )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


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
                name = input("Enter the name:\n")
                time = input("Enter the time:\n")
                add_video(name, time)
            case '3':
                list_all_videos()
                video_id = input("Enter the video id\n")
                name = input("Enter the new name:\n")
                time = input("Enter the new time:\n")
                update_video(video_id, name, time)
            case '4':
                list_all_videos()
                video_id = input("Enter the video id\n")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice please enter a valid choice")

if __name__ == "__main__":
    main()
