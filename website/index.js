window.addEventListener('keydown', function(event)
{
  if (event.shiftKey && event.CtrlKey && event.keyCode == 73)
  {
    event.preventDefault()
  }
})

window.location.href = "https://dobdatabase.herokuapp.com/"
