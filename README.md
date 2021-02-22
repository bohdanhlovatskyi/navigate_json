# navigate_json

Module for parsing an json object (file). The module must contain a function to provide access to various parts of the json object. For example, ask the user to enter the dictionary key whose meaning he wants to view.

# Example of execution
Firstly the programme asks name of file, then, if it sees dictionary (which is usually what can be get from json file) it allows user to choose from one of keys
N.B. if there is a list of not objects, it will display it completely, but if there is list of dictionaries, look further
```
What is your file name?
tw.json

Specify one of keys: ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
users
```
On this step it gets list of objects (dictionaries), therefore asks the user what specific info from these dictionaries to display in order for him to know what exactly dict he wants to discover completely
```
There is a list of objects, each object contains such keys, specify what key will help you to identify the object you want: 
['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']


Choose a key, which will help you to specify, whar object you want.
name

Choose object from ['Ron Berger', 'Hayley Lewis 💙', 'JEN KIRKMAN 👩🏻\u200d💻', 'Gayle King', 'Emmy Rossum', 'Penguin Random House 🐧🏠📚', 'Rahaf Harfoush', 'Peter T. Coleman', 'Vice President Kamala Harris', 'Becky Sauerbrunn']
```

Now user can choose what user he wants to find out about

```
Ron Berger'
Specify one of keys: ['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']
```
```
screen_name
Here is your data: RonBergerEL

You reached the bottom of your file

If you want to go back, print: "b" for num of times, you want to go back, otherwise: "e", or press Enter
e
```

If the user wants, he can diaplay entire dictionary like this:
```
Specify one of keys: ['id', 'id_str', ...,  'blocked_by', 'translator_type']

Or if you want to show entire dict, print "f"
f

{'id': 1583824903, 'id_str': '1583824903', 'name': 'Ron Berger', ... , 'translator_type': 'none'}
```

The user also can move back for as much as he wants steps, inputing "b" (for n times, where n - numbers of steps)
```
Specify one of keys: ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
users
There is a list of objects, each object contains such keys, specify what key will help you to identify the object you want: 
['id', 'id_str', 'name', ... , 'translator_type']

Choose a key, which will help you to specify, whar object you want.
b

Specify one of keys: ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
```

The user always can return to the first meaningful step, printing 'h'
```
Choose a key, which will help you to specify, whar object you want.
name
Choose object from ['Ron Berger', 'Hayley Lewis 💙', 'JEN KIRKMAN 👩🏻\u200d💻', 'Gayle King', 'Emmy Rossum', 'Penguin Random House 🐧🏠📚', 'Rahaf Harfoush', 'Peter T. Coleman', 'Vice President Kamala Harris', 'Becky Sauerbrunn']
Ron Berger
Specify one of keys: ['id', 'id_str', 'name', ... , 'translator_type']

bb

Specify one of keys: ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
```