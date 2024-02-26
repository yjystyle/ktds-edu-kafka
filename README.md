# Kakfa on Kubernetes

> Container 기반 Kafka 교육자료 !!

본 교육은 Container를 기반으로 한 Kafka를 학습하는 과정으로 kubernetes 환경에서 kafka install수행하는 방법과 각각 모니터링 솔루션을 확인하는 방법을 알아보며 Spring Boot / Python 으로 실습한다.

문의: 송양종( yj.song@kt.com / ssongmantop@gmail.com )



# 1. 시작전에 ( [가이드 문서 보기](beforebegin/beforebegin.md) )

## 1) 실습 환경 준비

* MobaxTerm 설치
* Typora 설치
* 교육자료 Download
* 실습환경준비(Cloud)



# 2. Kafka 개념 ( [가이드 문서 보기](kafka/1.kafka-개념.md) )

## 1) Kafka 개요

* kafka 개요와 특징확인

## 2) Kafka 기본

* Kafka 구성요소인 Broker, Message, Producer, Consumer ,Topic 의 Concept 대해 확인
* Broker
  * Producer와 Consumer 사이에 존재하는 Broker 확인
* Partition과 Consumer Group
  * 병렬처리를 가능하게 하는 Partition과 수신 애플리케이션을 담당하는 Consumer Group
* Offset 관리
  * Conumer Group 단위로 Offset 을 관리
* Producer/Consumer Partitioning
  * Partion 별로 메세지 수신/ 발신 방법에 대한 개념 확인

## 3) Kafka Replication

* Replicas
  * Broker 장애시 수신 메시지 분실 방지를 위한 복제(Replication)
* ISR(In-Sync Replica)
  * ISR은 **현재 동기화 상태에 있는** **리플리케이션**
* Producer Ack
  * Replication 구조에서 Producer 메시지 송신 타이밍을 결정하는 Ack 설정



# 3. Kafka Hands-in ( [가이드 문서 보기](kafka/2.kafka-hands-in.md) )

## 1) Strimzi

* Strimzi / Strimzi Operator 란?

## 2) Strimzi Operator install

* Strmzi download 및 install 방법

## 3) Kafka Cluster 생성

* Kafka Cluster 생성
* Kafka User 생성
* Kafka Topic 생성

## 4) Accessing Kafka

* Broker 접근 방식의 이해
* Internal / External Access 이해
* Internal Access Test
* Node Port 구성 / External Access Test

## 5) Python Test

* Python Client (Kubernetes / Docker 이용) 설치
* Internal Access / External Access

## 6) Strimzi Clean up

## 7) Java - Spring Boot

* 개인별로 할당된 Topic 확인
* kafka-consumer 실습
* kafka-producer 실습





# 4. Kafka Hands-in 2 ( [가이드 문서 보기](kafka/3.kafka-hands-in2.md) )

## 1) 테스트 환경준비

* Bastion server 준비
* Ptyhon Container 준비

## 2) Rebalancing Round

* Stop The World 내용 확인
* Rebalancing 시나리오
* 시나리오 테스트 수행

## 3) Producer 실습

* Producer 관련 실습
* key 와 partition 관계 이해
* 전송보장과  ack
* Sender 동작

## 4) Consumer 실습

* Consumer 관련 실습
* auto.offset.reset
* poll method
* Auto / Manual Commit





# 별첨. Cloud Setup ( [가이드 문서 보기](cloud-setup/cloud-setup.md) )

## 1) Bastion Server Setup

* kubernetes Install (k3s)
* Helm Install
* 기타 Tool Setup

## 2) Kafka Setup(Strimzi) on Cloud

* Strimzi Cluster Operator Install
* Kafka Cluster 생성
* KafkaUser / KafkaTopic 생성
* Monitoring 환경구축 (Kafka Exporter / Prometheus / Grafana / Kafdrop )
