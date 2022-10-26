const body = document.querySelector('body')
const obj = {
  logThis : function() {
    console.log(this)
  },
  setTime : function () {
    setTimeout(this.logThis, 2000)
  },
  addEvent : function(){
    body.addEventListener('click',this.logThis)
  }
}
obj.logThis()
obj.setTime()
obj.addEvent()

//forEach 같은 경우?
const obj2 = {
  method : function() {
    [1,2,3].forEach(function(){
      console.log(this)
    }, this)
    //두 번째 인자로 this를 넣어주는 경우, method f를 가리키게 됨
    //이게 없다면 window로 날아가게 됨
  }
}
