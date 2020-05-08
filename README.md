# essay_correction
2019년 8월 한 달간 영어논문교정 기업 'W'기업과의 협업 프로젝트 (2019 빅데이터 청년인재 과정 中)

## 학술 영문 자동 교정 서비스
세계 언어 서비스 시장은 CAGR 7.76%로 꾸준히 성장해왔으며, 2019년 시장규모는 60조 (US$ 496억)를 초과할 것으로 전망된다. 시장의 경쟁이 심해지면서 언급되는 문제점은 다음과 같다.

*문제점
국내외 다수의 LSP는 여러 나라에 걸쳐 서비스를 제공 → 국내 시장 규모의 정확한 추산 불가.
동일한 서비스의 경쟁사 多 (해외 업체의 국내 서비스 & 후발 업체의 시장 진입 증가).
Manual 한 교정 방식 → 높은 시간과 비용이 소요, 대학·연구기관 등에 소비층 제한.

이러한 문제점에서 경쟁우위를 갖기 위해, 차별화된 서비스와 소비층 확대의 필요성이 높아지고 있다.

학술 영문 검사의 경우, academic writing에서 선호하는 표현과 discipline-specific terms가 존재하기 때문에 일반 writing 교정과 구분 필요하다. 이러한 이유로 학술 영어는 editor에 의한 manual한 교정 방식에 의존한다.

그러므로 Academic 영어 위한 자동 교정 시스템/서비스 구축을 통한 시장 선점이 필요하다.

## 데이터
기존 W기업의 서비스는 숙련된 논문 교정가가 용도에 따라 논문을 하나부터 열까지 전부 수정해주는 서비스였다.
이로 인한 문제점은 기초적인 문법이나 단어 선택 교정 과정에서 불필요한 시간이 소요된다는 것이었다.
그렇기해 W기업은 사용자와 교정가의 시간을 단축시킬 수 있는 lite한 자동 교정 서비스를 제작하기를 원했다.

우리 팀은 이러한 서비스를 제작하기 위해 기존 영문 교정 데이터 (교정 전, 교정 후)를 수집하여,
단어-단어 / 단어-숙어 / 숙어-단어 / 숙어-숙어 로 데이터를 dictionaty 형태로 분류하였다.
또한 교정 후보가 여러 단어(숙어)일 경우 출현 빈도수에 따라 dict의 우선 순위를 분류했다.

## 코드 설명
프로젝트 초기엔 딥러닝 알고리즘(ex:RNN)을 이용하고 싶었지만 프로젝트의 목표와 기간, 컴퓨팅 파워 등으로
비교적 간단한 코드로 진행하였다.

input으로 사용자가 입력한 영어 문장이 들어간다. 그 후 미리 정리해놓은 dict를 거쳐
문장 안에 dict의 key값이 있다면 item의 후보군을 출력해준다. (1,2,3 ... 형식)

사용자가 수정을 원하여 item 값 중 원하는 값을 입력하면, 그 문자를 수정해주는 형식의 대화형 코드이다.
