function navClick(){
  //getting button to control
  let openbtn=document.getElementsByClassName("openbtn")[0];
  //toggling button icons 
  openbtn.classList.toggle("fa-bars");
  openbtn.classList.toggle("fa-times");
  //toggling width of sidenav
  let sidebar=document.getElementById("mySidebar");
  let cStyle = getComputedStyle(sidebar);
  let navWidth = cStyle.getPropertyValue("width"); 
  if(navWidth=="65px")
    sidebar.style.width="250px";
  else if(navWidth=="250px")
    sidebar.style.width="65px"
  //toggling span elements visiblility
  let tag=document.getElementsByTagName("span");
  for(let i=1;i<6;i++)
  {
    tag[i].classList.toggle("d-none");
  }
}