
function func() {
  f();
  function f() {
    console.warn('sfd');
  }
}

func()
