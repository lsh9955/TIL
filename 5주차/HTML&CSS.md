## HTML

웹 표준

- W3C WHATWG

HTML

Hyper Text Markup Language

웹 페이지를 작성하기 위한 언어

- html
    - 문서 최상위 요소
- head
    - 문서 메타데이터
- body
    - 실제 화면구성 내용

속성을 작성할 때

```html
<a href="https://www~"></a>
	중간에 공백X, 쌍따옴표 사용
```

시맨틱 태그

- 태그가 특정 목적, 역할 및 가치를 가지는 것
- 대표적인 시맨틱
    - header, nav, aside, section, article, footer

DOM 트리

- html은 텍스트 파일임
- 브라우저에서 html을 렌더링 하기 위한 구조

텍스트 요소

- <i>,<em> 기울임 글씨 요소
- <hr> 수평선, 문단 레벨에서 주제의 분리를 의미
- <pre> html작성 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지함
- <blockquote> 텍스트가 긴 인용문. 주로 들여쓰기를 한 것으로 표현됨
- <form>
    - action - 데이터를 보낼 url
    - method - http 메서드(get,post)
    - enctype - method가 post인 경우 데이터 유형
- <input>
    - name - form control에 적용되는 이름
    - value  - form control에 적용되는 값
    - <label>
        - imput에 id속성을, label에 for속성을 써서 상호 연관이 가능
    - 타입에 따라 기본적인 검증 활용이 가능
        - email - 이메일 형식이 아니면 제출이 불가
        - number - min,max 속성을 활용해 숫자 범위 설정이 가능
        - file - accept 속성을 활용해 파일 타입 지정이 가능
        

## CSS

- 속성과 값, 하나의 쌍으로 이루어진 선언을 진행함
- 각 쌍은 선택한 요소의 속성과 속성에 부여할 값을 의미함
- 선택자 유형
    - 기본 선택자
        - 요소 선택자
            - html 태그를 직접 선택
        - class 선택자
            - .으로 시작, 해당 클래스가 적용된 항목을 선택
        - id 선택자
            - #으로 시작하며, 하나의 문서에 1번만 사용
        
    - 결합자
    - 의사 선택자
        - 의사 클래스(:)를 사용한 표기
        - 의사 클래스 - 클래스가 정의된 것처럼 간주함
        - ex) a:link라 하면 a태그의 클래스인 link가 선언된 것 처럼 생각하고 선택자를 만드는 것
- 적용 우선순위
    - !important>인라인>id>class,pseudo-class>요소,pseudo-element
- css 상속
    - 상속이 되는 것
        - text 관련 요소
            - font,color,text-align
        - opacity
        - visibility
    - 상속이 되지 않는 것
        - box model 관련 요소
            - width, height, margin 등
        - position 관련 요소
            - top,right,z-index 등
- 결합자
    - 자손 결합자 (공백)
        - 하위의 모든 요소
    - 자식 결합자 (>)
        - 바로 아래의 요소
    - 일반 형제 결합자 (~)
        - 형제 요소 중 뒤에 위치하는 모든 요소
    - 인접 형제 결합자 (+)
        - 형제 요소 중 바로 뒤의 요소
- box model 구성
    - content
    - padding
    - border
    - margin
        - 배경색을 지정할 수 없음
    - 보통 box-sizing은 content-box 이지만, 일반적으로 border까지의 너비를 너비로 보길 원함
        - 이럴 경우 box-sizing을 border-box로 설정
- 블록 레벨 요소/인라인 레벨 요소
    - 블록레벨 요소
        - div, ul, ol, li, p, hr, form
        - 문단을 나누거나 문단을 만드는 요소들
- display : none과 visibility : hidden의 차이?
    - display : none은 화면표시X,공간도 없음
    - visibility : hidden은 공간은 차지하나 화면에 표시만 안됨
- CSS position
    - relative
        - 자기 자신의 static위치를 기준으로 이동
        - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
    - absolute
        - 가까이 있는 부모/조상 요소를 기준으로 이동
        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    - fixed
        - 공간을 차지하지 않음
        - 공간을 차지하게 하려면 sticky를 써야함
    - float
        - 박스를 왼쪽/오른쪽으로 이동시켜 인라인요소들이 주변을 wrapping하도록 함
        - 요소가 normal flow를 벗어남
    - flex box
        - flexbox를 사용하는 이유?
            - 없이는 수직 정렬, 아이템의 너비와 높이 혹은 간격을 동일하게 배치하는 것이 어려웠음
        - 행과 열로 아이템 배치
        - 축
            - main axis
            - cross axis
        - 구성 요소
            - flex container
            - flex item
        - 속성
            - 배치 설정
                - flex-direction
                    - 역방향의 경우 html 태그 선언 순서와 다름
                    - row
                    - row-reverse
                    - column
                    - column-reverse
                - flex-wrap
                    - wrap
                    - nowrap(default)
                - flex-flow
                    - flex-direction과 flex-wrap을 합친 것
            - justify-content
                - main axis를 기준으로 공간을 배분함
                    - flex-start
                    - flex-end
                    - center
                    - space-between
                        - 가운데 여백들을 동일하게 나눔(양쪽 끝 요소는 맨 가장자리에 붙게 됨)
                    - space-round
                        - 각 요소의 양쪽 여백들이 동일하게 나눠지게 됨(1:2:2:1)
                    - space-evenly
                        - 모든 여백들이 동일하게 나눠짐(양쪽 끝 요소가 가장자리에 붙지 않음)
                - align-content
                    - cross-axis를 기준으로 공간 배분
                        - flex-start
                        - flex-end
                        - center
                        - space-between
                        - space-evenly
                        - space-around
                - align-items
                    - 모든 아이템을 cross axis 기준으로 정렬
                    - stretch (default)
                    - flex-start
                    - flex-end
                    - center
                    - baseline
                - align-center
                    - 개별 아이템에 적용
                    - stretch
                    - flex-start
                    - flex-end
                    - center
                - 기타
                    - flex-grow
                    - order
    
    ## bootstrap
    
    - cdn
        - 컨텐츠를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에 데이터를 제공하는 시스템
    - grid system
        - 12개의 column, 6개의 grid breakpoints로 이루어져 있음
        - column
            - 실제 컨텐츠를 포함하는 부분
        - gutter
            - 칼럼과 칼럼 사이의 공간
        - container
            - column들을 담고 있는 공간
        - grid breakpoints
            - 반응형에 사용됨
            - col-A-B
            - A에는 언제 변화할지에 대한 내용이 담김
            - B에는 1~12의 값 중 하나가 들어감. 얼마나 자리를 차지할 지에 대해 정의할 수 있음
