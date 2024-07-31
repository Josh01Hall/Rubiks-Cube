import visualise, move_window, threading, installs


visualiser = visualise.Cube_Renderer()
visualiser_thread = threading.Thread(target=visualiser.render)
visualiser_thread.start()
mover = move_window.Move_GUI(visualiser)