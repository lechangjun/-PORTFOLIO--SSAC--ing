# Kibana Query

# data 확인
GET kibana_sample_data_flights/_search

# 매핑 정보 확인
GET kibana_sample_data_flights/_mapping

# 비행기 티켓값 오름 차순 정리
POST kibana_sample_data_flights/_search
{
    "sort":
    [{"AvgTicketPrice": {"order": "asc"}}]
}

# 비행기 지연 사유가 날씨인 경우
POST kibana_sample_data_flights/_search
{
    "query": {
        "match": {
            "FlightDelayType": "Weather Delay"
        }
    }
}

# 출발 국가가 미국인 곳 검색
POST kibana_sample_data_flights/_search
{
    "query": {
        "match": {
            "OriginCountry": "US"
        }
    }
}

# 지연 시간이 180분 이상인 경우 검색
POST kibana_sample_data_flights/_search
{
    "query": {
        "range": {
            "FlightDelayMin": {
                "gte" : 180
            }
        }
    }
}

# 비행기 티켓값 내림 차순 정리
POST kibana_sample_data_flights/_search
{
    "query": {
        "term": {
            "FlightDelayType": "Weather Delay"
        }
    },
    "sort":
    [{"AvgTicketPrice": {"order": "desc"}}]
}

# 캐나다로 가는 항공편의 비행 거리의 평균
GET kibana_sample_data_flights/_search?size=0
{
    "query": {
        "constant_score": {
            "filter": {
                "match": {
                    "DestCountry": "CA"
                }
            }
        }
    },
    "aggs": {
        "average_balance": {
            "avg": {
                "field": "DistanceKilometers"
            }
        }
    }
}