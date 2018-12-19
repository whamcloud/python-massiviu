workflow "New workflow" {
  on = "push"
  resolves = ["Start Mock Container"]
}

action "Start Mock Container" {
  uses = "actions/docker/cli@76ff57a"
  args = "docker run -dit --name mock -v $(pwd):/mockdir --cap-add=SYS_ADMIN --privileged imlteam/mock"
}
