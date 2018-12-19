workflow "New workflow" {
  on = "push"
  resolves = ["Start Mock Container"]
}

action "Start Mock Container" {
  uses = "actions/docker/cli@master"
  args = "run -dit --name mock -v $(pwd):/mockdir --cap-add=SYS_ADMIN --privileged imlteam/mock"
}
