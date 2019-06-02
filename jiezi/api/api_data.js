define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./api/main.js",
    "group": "D__github_Jiezi_jiezi_api_main_js",
    "groupTitle": "D__github_Jiezi_jiezi_api_main_js",
    "name": ""
  },
  {
    "type": "POST",
    "url": "/accounts/add_set",
    "title": "Add set",
    "description": "<p>Make an copy of an existing character set in user's library</p>",
    "group": "accounts",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "set_id",
            "description": "<p>the id of the set to be added</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "type": "String",
            "optional": false,
            "field": "msg",
            "description": "<p>the detail of the exception</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./accounts/views.py",
    "groupTitle": "accounts",
    "name": "PostAccountsAdd_set"
  },
  {
    "type": "POST",
    "url": "/accounts/delete_character",
    "title": "Delete character",
    "group": "accounts",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "character_id",
            "description": "<p>the Jiezi id of the character</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "set_id",
            "description": "<p>(optional) the id of the user set for the character to be deleted from, otherwise the character will be delete from all user sets of the current user</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./accounts/views.py",
    "groupTitle": "accounts",
    "name": "PostAccountsDelete_character"
  },
  {
    "type": "POST",
    "url": "/accounts/delete_set",
    "title": "Delete set",
    "description": "<p>Delete a user set</p>",
    "group": "accounts",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "set_id",
            "description": "<p>the id of the user set to be deleted from</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_delete_characters",
            "defaultValue": "False",
            "description": "<p>(optional) false will not delete the characters in this set from the user library, even if they don't belong to any sets</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./accounts/views.py",
    "groupTitle": "accounts",
    "name": "PostAccountsDelete_set"
  },
  {
    "type": "POST",
    "url": "/accounts/get_available_sets",
    "title": "Get available sets",
    "description": "<p>Get available existing character sets to add</p>",
    "group": "accounts",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "sets",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "string",
            "optional": false,
            "field": "sets.name",
            "description": "<p>the name of the set to display</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "sets.id",
            "description": "<p>the id to send back if the set is added</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"sets\": [\n        {\n            \"name\": \"Numbers\",\n            \"id\": 2\n        },\n        {\n            \"name\": \"Integrated Chinese I\",\n            \"id\": 4\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./accounts/views.py",
    "groupTitle": "accounts",
    "name": "PostAccountsGet_available_sets"
  }
] });