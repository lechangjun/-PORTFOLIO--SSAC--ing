# 리눅스 서버 60초안에 상황파악하기

Date: August 25, 2021 → August 26, 2021


![image](https://user-images.githubusercontent.com/68671394/134755847-0557ed24-f13b-4562-86ec-cd90e3f04f9b.png)

## 10. top

```bash
$ top
top - 00:15:40 up 21:56,  1 user,  load average: 31.09, 29.87, 29.92
Tasks: 871 total,   1 running, 868 sleeping,   0 stopped,   2 zombie
%Cpu(s): 96.8 us,  0.4 sy,  0.0 ni,  2.7 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  25190241+total, 24921688 used, 22698073+free,    60448 buffers
KiB Swap:        0 total,        0 used,        0 free.   554208 cached Mem

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 20248 root      20   0  0.227t 0.012t  18748 S  3090  5.2  29812:58 java
  4213 root      20   0 2722544  64640  44232 S  23.5  0.0 233:35.37 mesos-slave
 66128 titancl+  20   0   24344   2332   1172 R   1.0  0.0   0:00.07 top
  5235 root      20   0 38.227g 547004  49996 S   0.7  0.2   2:02.74 java
  4299 root      20   0 20.015g 2.682g  16836 S   0.3  1.1  33:14.42 java
     1 root      20   0   33620   2920   1496 S   0.0  0.0   0:03.82 init
     2 root      20   0       0      0      0 S   0.0  0.0   0:00.02 kthreadd
     3 root      20   0       0      0      0 S   0.0  0.0   0:05.35 ksoftirqd/0
     5 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H
     6 root      20   0       0      0      0 S   0.0  0.0   0:06.94 kworker/u256:0
     8 root      20   0       0      0      0 S   0.0  0.0   2:38.05 rcu_sched
```

`top` 명령어는 위에서 체크해본 다양한 측정치를 쉽게 체크할 수 있다. 시스템 전반적으로 값을 확인하기 쉽다는 장점이 있다. 화면이 지속적으로 바뀌는 점 떄문에 패턴을 찾는것이 어렵다. 일시적으로 멈추는 현상을 잡기 위해서도 화면을 주기적으로 빠르게 멈춰주지 않으면 찾기 힘들다(Ctrl+S는 업데이트를 중지시키고, Ctrl+Q는 다시 시작시킨다), 그리고 화면이 지워져버린다.
