import tkinter  #thu vien do hoa

#setup
player1 = 'X'
player2 = 'O'
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
turns = 0
game_over = False
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"

#window setup
window = tkinter.Tk()  #tao cua so window
window.title("Co ca ro")
window.resizable(False,False)

def CheckWinner(curr_player):
    #check hang ngang
    if board[0][0]["text"] == board[0][1]["text"] == board[0][2]["text"] == curr_player:
        return True
    if board[1][0]["text"] == board[1][1]["text"] == board[1][2]["text"] == curr_player:
        return True
    if board[2][0]["text"] == board[2][1]["text"] == board[2][2]["text"] == curr_player:
        return True
    #check hang doc
    if board[0][0]["text"] == board[1][0]["text"] == board[2][0]["text"] == curr_player:
        return True
    if board[0][1]["text"] == board[1][1]["text"] == board[2][1]["text"] == curr_player:
        return True
    if board[0][2]["text"] == board[1][2]["text"] == board[2][2]["text"] == curr_player:
        return True
    #cheo
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] == curr_player:
        return True
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] == curr_player:
        return True


def SetTitle(row,column):
    global curr_player
    global turns,game_over
    
    if board[row][column]["text"] != "":
         return
    
    if game_over:
        return
    
    board[row][column]["text"] = curr_player
    turns += 1

    #ktra nguoi thang
    if (CheckWinner(curr_player)):
        label.config(text=curr_player + ' la nguoi chien thang!!!',foreground= color_yellow)
        game_over = True
        return
    
    #hoa
    if turns == 9:
        game_over = True
        label.config(text = "Ca 2 nguoi choi hoa nhau!!!",foreground= color_yellow)
        return
    
    if curr_player == player1:
        curr_player = player2
    else:
        curr_player = player1
    
    label["text"] = "Luot cua nguoi choi " + curr_player

    
def NewGame():
    global turns,game_over
    turns = 0
    game_over = False
    label["text"] = "Luot cua nguoi choi " + curr_player
    for row in range(3):
        for col in range(3):
            board[row][col].config(text="",foreground=color_blue,background=color_gray)
    return


if __name__ == "__main__":
    frame = tkinter.Frame(window)
    curr_player = player1
    #tao label luot choi
    if curr_player == player1:
        label = tkinter.Label(frame,text="Luot cua nguoi choi X",font=("Consolas",18),
                              background = color_gray,foreground="white")
    else:
        label = tkinter.Label(frame,text="Luot cua nguoi choi O",font=("Consolas",18),
                              background = color_gray,foreground="white")
    label.grid(row=0,column=0,columnspan=3,sticky="we")  #them label vao grid

    #tao 9 o button
    for row in range(3):
        for column in range(3):
                board[row][column] = tkinter.Button(frame,text="",font=("Consolas",50,"bold"),
                                                    background = color_gray,foreground=color_blue,
                                                    width=5,height=1,command= lambda row=row,column = column:SetTitle(row,column))
                board[row][column].grid(row = row+1, column = column) #them button vao grid. label vi tri 00 nen button dich xuong 1 hang
    
    #tao nut restart
    re_button = tkinter.Button(frame,text="Restart",font=("Consolas",20),background="black",
                               foreground="white",command=NewGame)
    re_button.grid(row = 4,column=0,columnspan=3,sticky="we")


    frame.pack()    #dan frame vao window
    window.mainloop()  #loop window toi khi bam exit