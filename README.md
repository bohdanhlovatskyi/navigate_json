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
On this step there is a list of objects in yout json file, please specify what category you need to identify what onbject is interesting for you
ere is an example of what the object contains: ['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']
name
We get this category: name. Please wait.

['Ron Berger', 'Hayley Lewis 💙', 'JEN KIRKMAN 👩🏻\u200d💻', 'Gayle King', 'Emmy Rossum', 'Penguin Random House 🐧🏠📚', 'Rahaf Harfoush', 'Peter T. Coleman', 'Vice President Kamala Harris', 'Becky Sauerbrunn']
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
```

As far as I'm convinced there is no need in making going backwards available, because json files are not often very 'deep', so it would not be really uncomfortable to start again