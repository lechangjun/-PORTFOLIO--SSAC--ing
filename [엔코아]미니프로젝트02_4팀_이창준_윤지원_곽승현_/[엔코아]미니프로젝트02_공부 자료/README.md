# 리눅스 서버 60초안에 상황파악하기

Date: August 25, 2021 → August 26, 2021

### 

넷플릭스의 [Linux performance analysis in 60,000ms](https://medium.com/netflix-techblog/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)에 대해서 부분적으로 번역한 글입니다.

리눅스 서버에 성능 이슈로 인해서 로그인했을 때 우리가 가장 먼저 체크해봐야할 사항은 어떤것들일까?

넷플릭스는 많은 사람들이 알고 있는것 처럼 아마존 EC2 리눅스 서버를 사용하고 있다. 이런 대규모 서버를 모니터링하고 성능을 체크하는데에는 툴을 사용하는데 클라우드 전체의 모니터링에는 [Atlas](https://medium.com/netflix-techblog/introducing-atlas-netflixs-primary-telemetry-platform-bd31f4d8ed9a), 하나의 EC2 instance의 성능체크에는 [Vector](https://medium.com/netflix-techblog/introducing-vector-netflixs-on-host-performance-monitoring-tool-c0d3058c3f6f)를 사용한다. 이 툴을 이용하면 대부분의 이슈는 해결 가능하지만, 가끔씩은 EC2 instance에 로그인해서 리눅스의 표준적인 성능 체크 툴을 사용할때가 있다.

## 첫 60초

이 글에서는 1분 안에 표준적인 리눅스 환경에서 CLI를 이용해 어떤 것들을 확인할지에 대해서 순서대로 알아볼것이다.

`$ uptime
$ dmesg | tail
$ vmstat 1
$ mpstat -P ALL 1
$ pidstat 1
$ iostat -xz 1
$ free -m
$ sar -n DEV 1
$ sar -n TCP,ETCP 1
$ top`
