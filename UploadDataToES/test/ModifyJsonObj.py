search_doc_a = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "800"
              }
            },
            {
              "match_phrase": {
                "param3": ""
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_a["query"]["constant_score"]["filter"]["bool"]["must"][1]["match_phrase"]["param3"] = 'name=\"Command\"; value=\"route print\"'

search_doc_b = {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "event_id": "4103"
            }
          },
          {
            "match_phrase": {
              "powershell.param.value": ""
            }
          }
        ]
      }
    }
  }

search_doc_b["query"]["bool"]["must"][1]["match_phrase"]["powershell.param.value"] = "test2"

print(search_doc_a)

print(search_doc_b)