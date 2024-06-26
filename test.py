import visualise, time


render = visualise.Cube_Renderer()

def test():
    time.sleep(3)
render.selected_turn = [[0, 1], 90]

#test_thread = threading.Thread(target=test)
#test_thread.start()
render.selected_turn = [[5, 1], 90]
render.render()