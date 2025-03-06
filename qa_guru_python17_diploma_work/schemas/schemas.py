search_movie_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "original_query": {
      "type": "string"
    },
    "suggestion": {
      "type": "null"
    },
    "status": {
      "type": "string"
    },
    "meta": {
      "type": "object",
      "properties": {
        "items_count": {
          "type": "integer"
        },
        "items_limit": {
          "type": "integer"
        },
        "items_offset": {
          "type": "integer"
        }
      },
      "required": [
        "items_count",
        "items_limit",
        "items_offset"
      ]
    },
    "items": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": {}
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": {}
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "null"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": {}
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "image_1x": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "text_right": {
                      "type": "string"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "text_color_right": {
                      "type": "string"
                    },
                    "background_color": {
                      "type": "string"
                    },
                    "background_color_right": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "size": {
                      "type": "string"
                    },
                    "structure": {
                      "type": "string"
                    },
                    "under_logo_position": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "alias",
                    "image_1x",
                    "text",
                    "text_right",
                    "text_color",
                    "text_color_right",
                    "background_color",
                    "background_color_right",
                    "type",
                    "size",
                    "structure",
                    "under_logo_position"
                  ]
                }
              ]
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": {}
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "alias": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "episodes_count": {
                      "type": "integer"
                    },
                    "episodes_uids": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "episodes_titles": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        },
                        {
                          "type": "string"
                        }
                      ]
                    },
                    "rating_age": {
                      "type": "string"
                    },
                    "special": {
                      "type": "boolean"
                    },
                    "play_last_season": {
                      "type": "boolean"
                    },
                    "is_premier": {
                      "type": "boolean"
                    },
                    "downloadable": {
                      "type": "boolean"
                    },
                    "drm_encrypted": {
                      "type": "boolean"
                    },
                    "enabled_for_partner": {
                      "type": "boolean"
                    },
                    "for_kids": {
                      "type": "boolean"
                    },
                    "hot_content": {
                      "type": "boolean"
                    },
                    "in_subscription": {
                      "type": "boolean"
                    },
                    "is_disabled": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_maxmind_proxy_enabled": {
                      "type": "boolean"
                    },
                    "is_preview": {
                      "type": "boolean"
                    },
                    "is_top250": {
                      "type": "boolean"
                    },
                    "premium": {
                      "type": "boolean"
                    },
                    "standart": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "_id",
                    "uid",
                    "alias",
                    "number",
                    "title",
                    "episodes_count",
                    "episodes_uids",
                    "episodes_titles",
                    "rating_age",
                    "special",
                    "play_last_season",
                    "is_premier",
                    "downloadable",
                    "drm_encrypted",
                    "enabled_for_partner",
                    "for_kids",
                    "hot_content",
                    "in_subscription",
                    "is_disabled",
                    "is_free",
                    "is_maxmind_proxy_enabled",
                    "is_preview",
                    "is_top250",
                    "premium",
                    "standart"
                  ]
                }
              ]
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "download_options": {
              "type": "string"
            },
            "downloadable": {
              "type": "boolean"
            },
            "drm_encrypted": {
              "type": "boolean"
            },
            "duration": {
              "type": "integer"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "genres": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    },
                    "slug": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "title",
                    "slug"
                  ]
                }
              ]
            },
            "genres_string": {
              "type": "string"
            },
            "horizontal": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "hot_content": {
              "type": "boolean"
            },
            "is_maxmind_proxy_enabled": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "is_top250": {
              "type": "boolean"
            },
            "is_4k": {
              "type": "boolean"
            },
            "is_51": {
              "type": "boolean"
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "meta": {
              "type": "array",
              "items": {}
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "premium": {
              "type": "boolean"
            },
            "quote": {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "text": {
                  "type": "string"
                }
              },
              "required": [
                "source",
                "text"
              ]
            },
            "quote_source": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "summary": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "trailer_src": {
              "type": "string"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "video_cover": {
              "type": "string"
            },
            "web_url": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "rating_start": {
              "type": "number"
            }
          },
          "required": [
            "_cls",
            "_id",
            "uid",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "download_options",
            "downloadable",
            "drm_encrypted",
            "duration",
            "enabled_for_partner",
            "for_kids",
            "genres",
            "genres_string",
            "horizontal",
            "hot_content",
            "is_maxmind_proxy_enabled",
            "is_premier",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_preview",
            "is_top250",
            "is_4k",
            "is_51",
            "logotype",
            "meta",
            "packshot",
            "play_last_season",
            "playback_options",
            "premium",
            "quote",
            "quote_source",
            "rating_age",
            "release_date",
            "slug",
            "special",
            "standard",
            "summary",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "trailer_src",
            "vertical",
            "video_cover",
            "web_url",
            "year",
            "rating_start"
          ]
        }
      ]
    }
  },
  "required": [
    "original_query",
    "suggestion",
    "status",
    "meta",
    "items"
  ]
}

switch_on_kids_mode_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "_id": {
      "type": "string"
    },
    "ab": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        },
        {
          "type": "object",
          "properties": {
            "exp_id": {
              "type": "integer"
            },
            "exp_name": {
              "type": "string"
            },
            "group_id": {
              "type": "integer"
            },
            "group_name": {
              "type": "string"
            }
          },
          "required": [
            "exp_id",
            "exp_name",
            "group_id",
            "group_name"
          ]
        }
      ]
    },
    "apple_id": {
      "type": "null"
    },
    "apple_info": {
      "type": "object"
    },
    "authentication_token": {
      "type": "string"
    },
    "contact_info": {
      "type": "object",
      "properties": {
        "email_is_confirmed": {
          "type": "boolean"
        }
      },
      "required": [
        "email_is_confirmed"
      ]
    },
    "country_code": {
      "type": "string"
    },
    "current_country_code": {
      "type": "string"
    },
    "date_created": {
      "type": "string"
    },
    "devices": {
      "type": "array",
      "items": {}
    },
    "email": {
      "type": "string"
    },
    "externals": {
      "type": "array",
      "items": {}
    },
    "facebook_id": {
      "type": "null"
    },
    "facebook_info": {
      "type": "object"
    },
    "google_id": {
      "type": "null"
    },
    "is_registered": {
      "type": "boolean"
    },
    "language": {
      "type": "object",
      "properties": {
        "audio": {
          "type": "string"
        },
        "content_lang": {
          "type": "array",
          "items": {}
        },
        "interface": {
          "type": "string"
        },
        "subtitles": {
          "type": "string"
        }
      },
      "required": [
        "audio",
        "content_lang",
        "interface",
        "subtitles"
      ]
    },
    "mf_info": {
      "type": "object"
    },
    "need_credentials": {
      "type": "boolean"
    },
    "phone": {
      "type": "string"
    },
    "pin_status": {
      "type": "string"
    },
    "profile_for_child": {
      "type": "boolean"
    },
    "profile_id": {
      "type": "string"
    },
    "promo_manager": {
      "type": "boolean"
    },
    "segmentation_id": {
      "type": "string"
    },
    "status_gdpr": {
      "type": "null"
    },
    "subscriptions": {
      "type": "array",
      "items": {}
    },
    "tags": {
      "type": "array",
      "items": {}
    },
    "traffic_source": {
      "type": "object"
    },
    "trial_is_available": {
      "type": "boolean"
    },
    "type": {
      "type": "string"
    },
    "virtual": {
      "type": "boolean"
    },
    "vk_id": {
      "type": "null"
    },
    "vk_info": {
      "type": "object"
    },
    "yandex_id": {
      "type": "null"
    },
    "yandex_info": {
      "type": "object"
    }
  },
  "required": [
    "_id",
    "ab",
    "apple_id",
    "apple_info",
    "authentication_token",
    "contact_info",
    "country_code",
    "current_country_code",
    "date_created",
    "devices",
    "email",
    "externals",
    "facebook_id",
    "facebook_info",
    "google_id",
    "is_registered",
    "language",
    "mf_info",
    "need_credentials",
    "phone",
    "pin_status",
    "profile_for_child",
    "profile_id",
    "promo_manager",
    "segmentation_id",
    "status_gdpr",
    "subscriptions",
    "tags",
    "traffic_source",
    "trial_is_available",
    "type",
    "virtual",
    "vk_id",
    "vk_info",
    "yandex_id",
    "yandex_info"
  ]
}

serial_description_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "_cls": {
      "type": "string"
    },
    "_id": {
      "type": "string"
    },
    "additional_content": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            },
            "announcement": {
              "type": "boolean"
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "start_id": {
              "type": "integer"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "description",
            "title",
            "uid",
            "video_src",
            "announcement",
            "restrictions",
            "start_id",
            "packshot"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            },
            "announcement": {
              "type": "boolean"
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "start_id": {
              "type": "integer"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "description",
            "title",
            "uid",
            "video_src",
            "announcement",
            "restrictions",
            "start_id",
            "packshot"
          ]
        }
      ]
    },
    "alias": {
      "type": "string"
    },
    "background": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "badges": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background_color": {
              "type": "string"
            },
            "background_color_right": {
              "type": "string"
            },
            "image_1x": {
              "type": "null"
            },
            "name": {
              "type": "string"
            },
            "size": {
              "type": "string"
            },
            "structure": {
              "type": "string"
            },
            "text": {
              "type": "string"
            },
            "text_right": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "text_color_right": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "under_logo_position": {
              "type": "boolean"
            }
          },
          "required": [
            "id",
            "alias",
            "background_color",
            "background_color_right",
            "image_1x",
            "name",
            "size",
            "structure",
            "text",
            "text_right",
            "text_color",
            "text_color_right",
            "type",
            "under_logo_position"
          ]
        }
      ]
    },
    "banner": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "null"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "budget": {
      "type": "null"
    },
    "cast": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "integer"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "null"
            },
            "character": {
              "type": "object",
              "properties": {
                "biography": {
                  "type": "string"
                },
                "main_character": {
                  "type": "boolean"
                },
                "name": {
                  "type": "string"
                },
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "string"
                },
                "start_id": {
                  "type": "integer"
                },
                "weight": {
                  "type": "null"
                }
              },
              "required": [
                "biography",
                "main_character",
                "name",
                "photo",
                "photo_app_section",
                "start_id",
                "weight"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        }
      ]
    },
    "color": {
      "type": "object",
      "properties": {
        "back_color_1": {
          "type": "string"
        },
        "back_color_2": {
          "type": "string"
        },
        "font_color": {
          "type": "string"
        }
      },
      "required": [
        "back_color_1",
        "back_color_2",
        "font_color"
      ]
    },
    "composers": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        }
      ]
    },
    "description": {
      "type": "string"
    },
    "directors": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        }
      ]
    },
    "display": {
      "type": "boolean"
    },
    "downloadable": {
      "type": "boolean"
    },
    "duration": {
      "type": "integer"
    },
    "duration_minutes": {
      "type": "string"
    },
    "enabled_for_partner": {
      "type": "boolean"
    },
    "facts": {
      "type": "array",
      "items": {}
    },
    "for_kids": {
      "type": "boolean"
    },
    "genres": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "slug": {
              "type": "string"
            }
          },
          "required": [
            "title",
            "slug"
          ]
        },
        {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "slug": {
              "type": "string"
            }
          },
          "required": [
            "title",
            "slug"
          ]
        }
      ]
    },
    "hashtags": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "alias",
            "title",
            "text_color",
            "url"
          ]
        }
      ]
    },
    "horizontal": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "horizontal_poster": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "in_subscription": {
      "type": "boolean"
    },
    "is_4k": {
      "type": "boolean"
    },
    "is_51": {
      "type": "boolean"
    },
    "is_disabled": {
      "type": "boolean"
    },
    "is_free": {
      "type": "boolean"
    },
    "is_premier": {
      "type": "boolean"
    },
    "is_preview": {
      "type": "boolean"
    },
    "items": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "display": {
              "type": "boolean"
            },
            "downloadable": {
              "type": "boolean"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "items": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                }
              ]
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "num": {
              "type": "integer"
            },
            "number": {
              "type": "integer"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "publish": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "start_release_date": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "unavailable_by_geo": {
              "type": "boolean"
            },
            "unpublish": {
              "type": "integer"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "year": {
              "type": "integer"
            }
          },
          "required": [
            "_cls",
            "_id",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "display",
            "downloadable",
            "enabled_for_partner",
            "for_kids",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_premier",
            "is_preview",
            "items",
            "logotype",
            "num",
            "number",
            "packshot",
            "play_last_season",
            "playback_options",
            "publish",
            "rating_age",
            "release_date",
            "restrictions",
            "slug",
            "special",
            "standard",
            "start_release_date",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "uid",
            "unavailable_by_geo",
            "unpublish",
            "vertical",
            "year"
          ]
        },
        {
          "type": "object",
          "properties": {
            "_cls": {
              "type": "string"
            },
            "_id": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "background": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "badges": {
              "type": "array",
              "items": {}
            },
            "banner": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "description": {
              "type": "string"
            },
            "display": {
              "type": "boolean"
            },
            "downloadable": {
              "type": "boolean"
            },
            "enabled_for_partner": {
              "type": "boolean"
            },
            "for_kids": {
              "type": "boolean"
            },
            "in_subscription": {
              "type": "boolean"
            },
            "is_disabled": {
              "type": "boolean"
            },
            "is_free": {
              "type": "boolean"
            },
            "is_premier": {
              "type": "boolean"
            },
            "is_preview": {
              "type": "boolean"
            },
            "items": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id"
                          ]
                        }
                      ]
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "_cls": {
                      "type": "string"
                    },
                    "_id": {
                      "type": "string"
                    },
                    "announcement": {
                      "type": "boolean"
                    },
                    "badges": {
                      "type": "array",
                      "items": {}
                    },
                    "description": {
                      "type": "string"
                    },
                    "display": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer"
                    },
                    "free_for_authorized": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "packshot": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "string"
                        },
                        "image_15x": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "packshot_free": {
                      "type": "object",
                      "properties": {
                        "image_1x": {
                          "type": "null"
                        },
                        "image_15x": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "image_1x",
                        "image_15x"
                      ]
                    },
                    "playback_options": {
                      "type": "string"
                    },
                    "release_date": {
                      "type": "integer"
                    },
                    "restrictions": {
                      "type": "array",
                      "items": {}
                    },
                    "seo_text": {
                      "type": "string"
                    },
                    "start_id": {
                      "type": "integer"
                    },
                    "start_release_date": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "uid": {
                      "type": "string"
                    },
                    "unavailable_by_geo": {
                      "type": "boolean"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_cls",
                    "_id",
                    "announcement",
                    "badges",
                    "description",
                    "display",
                    "duration",
                    "free_for_authorized",
                    "is_free",
                    "num",
                    "number",
                    "packshot",
                    "packshot_free",
                    "playback_options",
                    "release_date",
                    "restrictions",
                    "seo_text",
                    "start_id",
                    "start_release_date",
                    "title",
                    "uid",
                    "unavailable_by_geo",
                    "web_url"
                  ]
                }
              ]
            },
            "logotype": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "num": {
              "type": "integer"
            },
            "number": {
              "type": "integer"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "play_last_season": {
              "type": "boolean"
            },
            "playback_options": {
              "type": "string"
            },
            "publish": {
              "type": "string"
            },
            "rating_age": {
              "type": "string"
            },
            "release_date": {
              "type": "integer"
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "slug": {
              "type": "string"
            },
            "special": {
              "type": "boolean"
            },
            "standard": {
              "type": "boolean"
            },
            "start_release_date": {
              "type": "string"
            },
            "subtitle": {
              "type": "string"
            },
            "thumbnail": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "null"
                },
                "image_15x": {
                  "type": "null"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "title": {
              "type": "string"
            },
            "title_original": {
              "type": "string"
            },
            "uid": {
              "type": "string"
            },
            "unavailable_by_geo": {
              "type": "boolean"
            },
            "unpublish": {
              "type": "integer"
            },
            "vertical": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "year": {
              "type": "integer"
            }
          },
          "required": [
            "_cls",
            "_id",
            "alias",
            "background",
            "badges",
            "banner",
            "description",
            "display",
            "downloadable",
            "enabled_for_partner",
            "for_kids",
            "in_subscription",
            "is_disabled",
            "is_free",
            "is_premier",
            "is_preview",
            "items",
            "logotype",
            "num",
            "number",
            "packshot",
            "play_last_season",
            "playback_options",
            "publish",
            "rating_age",
            "release_date",
            "restrictions",
            "slug",
            "special",
            "standard",
            "start_release_date",
            "subtitle",
            "thumbnail",
            "title",
            "title_original",
            "uid",
            "unavailable_by_geo",
            "unpublish",
            "vertical",
            "year"
          ]
        }
      ]
    },
    "items_total": {
      "type": "integer"
    },
    "kinopoisk_id": {
      "type": "string"
    },
    "locales": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "logotype": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "operators": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        }
      ]
    },
    "origin_countries": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "code": {
              "type": "string"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "code",
            "title"
          ]
        }
      ]
    },
    "packshot": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "play_last_season": {
      "type": "boolean"
    },
    "playback_options": {
      "type": "string"
    },
    "producers": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        }
      ]
    },
    "promo_content": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        },
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string"
            },
            "packshot": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            },
            "restrictions": {
              "type": "array",
              "items": {}
            },
            "title": {
              "type": "string"
            },
            "start_id": {
              "type": "integer"
            },
            "uid": {
              "type": "string"
            },
            "video_src": {
              "type": "string"
            }
          },
          "required": [
            "description",
            "packshot",
            "restrictions",
            "title",
            "start_id",
            "uid",
            "video_src"
          ]
        }
      ]
    },
    "publish": {
      "type": "string"
    },
    "quote": {
      "type": "string"
    },
    "quote_source": {
      "type": "string"
    },
    "rating_age": {
      "type": "string"
    },
    "rating_imdb": {
      "type": "number"
    },
    "rating_kp": {
      "type": "number"
    },
    "rating_start": {
      "type": "number"
    },
    "release_date": {
      "type": "integer"
    },
    "release_year_end": {
      "type": "null"
    },
    "release_year_start": {
      "type": "integer"
    },
    "restrictions": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            }
          },
          "required": [
            "id"
          ]
        }
      ]
    },
    "seo": {
      "type": "object",
      "properties": {
        "long_description": {
          "type": "string"
        },
        "short_description": {
          "type": "string"
        },
        "subject": {
          "type": "string"
        }
      },
      "required": [
        "long_description",
        "short_description",
        "subject"
      ]
    },
    "slug": {
      "type": "string"
    },
    "similar": {
      "type": "string"
    },
    "special": {
      "type": "boolean"
    },
    "special_description": {
      "type": "object",
      "properties": {
        "paragraph_1": {
          "type": "string"
        },
        "paragraph_2": {
          "type": "string"
        },
        "paragraph_3": {
          "type": "string"
        },
        "paragraph_4": {
          "type": "string"
        }
      },
      "required": [
        "paragraph_1",
        "paragraph_2",
        "paragraph_3",
        "paragraph_4"
      ]
    },
    "standard": {
      "type": "boolean"
    },
    "start_release_date": {
      "type": "string"
    },
    "subtitle": {
      "type": "string"
    },
    "thumbnail": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "null"
        },
        "image_15x": {
          "type": "null"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "title": {
      "type": "string"
    },
    "title_original": {
      "type": "string"
    },
    "trailer_src": {
      "type": "string"
    },
    "uid": {
      "type": "string"
    },
    "unavailable_by_geo": {
      "type": "boolean"
    },
    "unpublish": {
      "type": "integer"
    },
    "vertical": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "vertical_poster": {
      "type": "object",
      "properties": {
        "image_1x": {
          "type": "string"
        },
        "image_15x": {
          "type": "string"
        }
      },
      "required": [
        "image_1x",
        "image_15x"
      ]
    },
    "web_url": {
      "type": "string"
    },
    "weight": {
      "type": "null"
    },
    "writers": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        },
        {
          "type": "object",
          "properties": {
            "alias": {
              "type": "string"
            },
            "character": {
              "type": "object",
              "properties": {
                "photo": {
                  "type": "null"
                },
                "photo_app_section": {
                  "type": "null"
                }
              },
              "required": [
                "photo",
                "photo_app_section"
              ]
            },
            "filmography": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "photo": {
              "type": "object",
              "properties": {
                "image_1x": {
                  "type": "string"
                },
                "image_15x": {
                  "type": "string"
                }
              },
              "required": [
                "image_1x",
                "image_15x"
              ]
            }
          },
          "required": [
            "alias",
            "character",
            "filmography",
            "name",
            "photo"
          ]
        }
      ]
    },
    "year": {
      "type": "integer"
    }
  },
  "required": [
    "_cls",
    "_id",
    "additional_content",
    "alias",
    "background",
    "badges",
    "banner",
    "budget",
    "cast",
    "color",
    "composers",
    "description",
    "directors",
    "display",
    "downloadable",
    "duration",
    "duration_minutes",
    "enabled_for_partner",
    "facts",
    "for_kids",
    "genres",
    "hashtags",
    "horizontal",
    "horizontal_poster",
    "in_subscription",
    "is_4k",
    "is_51",
    "is_disabled",
    "is_free",
    "is_premier",
    "is_preview",
    "items",
    "items_total",
    "kinopoisk_id",
    "locales",
    "logotype",
    "operators",
    "origin_countries",
    "packshot",
    "play_last_season",
    "playback_options",
    "producers",
    "promo_content",
    "publish",
    "quote",
    "quote_source",
    "rating_age",
    "rating_imdb",
    "rating_kp",
    "rating_start",
    "release_date",
    "release_year_end",
    "release_year_start",
    "restrictions",
    "seo",
    "slug",
    "similar",
    "special",
    "special_description",
    "standard",
    "start_release_date",
    "subtitle",
    "thumbnail",
    "title",
    "title_original",
    "trailer_src",
    "uid",
    "unavailable_by_geo",
    "unpublish",
    "vertical",
    "vertical_poster",
    "web_url",
    "weight",
    "writers",
    "year"
  ]
}

tv_channels_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "channel_id": {
      "type": "null"
    },
    "selections": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "title",
            "alias",
            "url"
          ]
        }
      ]
    }
  },
  "required": [
    "title",
    "description",
    "channel_id",
    "selections"
  ]
}
