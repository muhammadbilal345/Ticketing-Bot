import re
import time
import threading
import pyautogui
import webbrowser
import tkinter as tk

class TicketingBotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ticketing Bot")
        self.main_heading = tk.Label(self, text="Ticketing Bot", font=("Helvetica", 16, "bold"))
        self.email_label = tk.Label(self, text="Email:")
        self.password_label = tk.Label(self, text="Password:")
        self.cvv_label = tk.Label(self, text="CVV:")
        self.how_many_times_label = tk.Label(self, text="How many times:")
        self.email_entry = tk.Entry(self, width=30)
        self.password_entry = tk.Entry(self, show="*", width=30)
        self.cvv_entry = tk.Entry(self, show="*", width=30)
        self.how_many_times_entry = tk.Entry(self, width=30)
        self.status_label = tk.Label(self, text="", fg="black")
        
        button_frame = tk.Frame(self)
        self.submit_button = tk.Button(button_frame, text="Submit", command=self.submit, bg="green", fg="white", width=6, height=1)
        self.exit_button = tk.Button(button_frame, text="Exit", command=self.exit_app, bg="red", fg="white", width=6, height=1)
        
        self.main_heading.grid(row=0, columnspan=2, pady=10)
        self.email_label.grid(row=1, column=0, sticky='w', padx=10)
        self.email_entry.grid(row=1, column=1, padx=10)
        self.password_label.grid(row=2, column=0, sticky='w', padx=10)
        self.password_entry.grid(row=2, column=1, padx=10)
        self.cvv_label.grid(row=3, column=0, sticky='w', padx=10)
        self.cvv_entry.grid(row=3, column=1, padx=10)
        self.how_many_times_label.grid(row=4, column=0, sticky='w', padx=10)
        self.how_many_times_entry.grid(row=4, column=1, padx=10)
        self.status_label.grid(row=5, columnspan=2)
        
        button_frame.grid(row=6, columnspan=2, pady=10)
        self.submit_button.grid(row=0, column=0, padx=10)
        self.exit_button.grid(row=0, column=1, padx=10)

        self.email = ""
        self.password = ""
        self.cvv = ""
        self.how_many_times = ""
        self.pyautogui_thread = None
        print(self.cvv)

    def is_valid_email(self, email):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, email)

    def is_valid_cvv(self, cvv):
        return cvv.isdigit() and len(cvv) == 4

    def is_valid_how_many_times(self, how_many_times):
        return how_many_times.isdigit()
    
    def submit(self):
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()
        self.cvv = self.cvv_entry.get()
        self.how_many_times = self.how_many_times_entry.get()

        if not self.is_valid_email(self.email):
            self.status_label.config(text="Invalid email format", fg="red")
        elif not self.password:
            self.status_label.config(text="Password cannot be empty", fg="red")
        elif not self.is_valid_cvv(self.cvv):
            self.status_label.config(text="Invalid CVV (must be a 4-digit number)", fg="red")
        elif not self.is_valid_how_many_times(self.how_many_times):
            self.status_label.config(text="Invalid how many times", fg="red")
        else:
            self.status_label.config(text="Submitted successfully", fg="green")
            self.start_pyautogui_thread()

    def start_pyautogui_thread(self):
        if self.pyautogui_thread is None or not self.pyautogui_thread.is_alive():
            self.pyautogui_thread = threading.Thread(target=self.pyautogui_script)
            self.pyautogui_thread.daemon = True
            self.pyautogui_thread.start()

    def pyautogui_script(self):
        def booking_with_login():
            time.sleep(5)
            cnt = 0
            webbrowser.open("https://www.ticketmaster.com")

            templates_to_check = [
                ('templates/sign_in_homepage.png', 3),
                ('templates/email.png', 4),
                ('templates/sign_in.png', 5),
                # ('templates/input_city.png', 3),
                ('templates/search_in_homepage.png', 5),
                ('templates/find_tickets.png', 3),
                ('templates/accept.png', 4),
                ('templates/agree.png', 3),
                # ('templates/select_tickets.png', 4),
                # ('templates/8_tickets.png', 1),
                ('templates/seat.png', 6),
                ('templates/next.png', 5),
                ('templates/cvv.png', 4),
                ('templates/yes_insurance.png', 2),
                # ('templates/got_it.png', 4),
                ('templates/agree_terms.png', 5)
                # ('templates/place_order.png', 2),

            ]

            accept_or_agree_template = ('templates/accept.png', 'templates/agree.png')

            for template, wait_time in templates_to_check:
                print(template)
                while True:
                    if template == 'templates/find_tickets.png':
                        time.sleep(5)
                        scroll_pixels = -500

                        while True:
                            pyautogui.scroll(scroll_pixels)
                            time.sleep(2)

                            template_location = pyautogui.locateOnScreen(template)

                            if template_location:
                                template_x, template_y = pyautogui.center(template_location)
                                pyautogui.click(template_x, template_y)
                                break
                        break
                        
                    elif template == 'templates/agree_terms.png':
                        time.sleep(2)
                        scroll_pixels = 1000

                        while True:
                            pyautogui.scroll(scroll_pixels)
                            time.sleep(2)

                            template_location = pyautogui.locateOnScreen(template)

                            if template_location:
                                template_x, template_y = pyautogui.center(template_location)
                                pyautogui.click(template_x, template_y)
                                break
                        break

                    elif template == 'templates/yes_insurance.png':
                        # time.sleep(2)
                        scroll_pixels = -700

                        while True:
                            pyautogui.scroll(scroll_pixels)
                            # time.sleep(2)
                            # template_image = 'insurance.png'
                            template_location = pyautogui.locateOnScreen(template)

                            if template_location:
                                template_x, template_y = pyautogui.center(template_location)
                                pyautogui.click(template_x, template_y)
                                break
                        break

                    # elif template == 'templates/yes_insurance.png':
                    #     # time.sleep(2)
                    #     scroll_pixels = -5000

                    #     pyautogui.scroll(scroll_pixels)
                    #     time.sleep(2)
                    #     # template_image = 'insurance.png'
                    #     template_location = pyautogui.locateOnScreen(template)

                    #     if template_location:
                    #         template_x, template_y = pyautogui.center(template_location)
                    #         pyautogui.click(template_x, template_y)
                    #     break

                    elif template in accept_or_agree_template:
                        for accept_agree_template in accept_or_agree_template:
                            template_location = pyautogui.locateOnScreen(accept_agree_template)
                            if template_location:
                                template_x, template_y = pyautogui.center(template_location)
                                pyautogui.click(template_x, template_y)
                                break
                        break

                    # print('temp', template)
                    else:
                        template_location = pyautogui.locateOnScreen(template)
                        print("else", template)
                        # time.sleep(2)

                        if template_location:
                            template_x, template_y = pyautogui.center(template_location)
                            pyautogui.click(template_x, template_y)
                            
                            if template == 'templates/email.png':
                                # email = 'juliabradpowers@gmail.com'
                                pyautogui.write(self.email)
                                pyautogui.hotkey('tab')
                                # password = 'Tickets111!'
                                pyautogui.write(self.password)

                            # if template == 'templates/input_city.png':
                            #     pyautogui.hotkey('ctrl', 'a')
                            #     pyautogui.press('delete')
                            #     city = 'Washington, DC'
                            #     pyautogui.write(city)
                            #     pyautogui.press("enter")

                            if template == 'templates/search_in_homepage.png':
                                pyautogui.press("enter")

                            if template == 'templates/cvv.png':
                                print("testing cvv", self.cvv)
                                pyautogui.write(self.cvv)
                            break
                        else:
                            cnt+=1
                            if cnt > 10:
                                cnt = 0
                                break
                            time.sleep(wait_time)


        def multiple_booking():
            cnt = 0
            for _ in range(int(self.how_many_times)-1):
                pyautogui.hotkey('ctrl', 't')
                time.sleep(2)
                url = "https://www.ticketmaster.com/search?sort=date%2Casc&radius=75&unit=miles&tab=events&daterange=allabc.com"
                pyautogui.write(url)
                pyautogui.press("enter")

                templates_to_check = [
                    ('templates/find_tickets.png', 4),
                    ('templates/accept.png',3),
                    ('templates/agree.png', 3),
                    # ('templates/select_tickets.png', 4),
                    # ('templates/8_tickets.png', 1),
                    ('templates/seat.png', 3),
                    ('templates/next.png', 4),
                    ('templates/cvv.png', 3),
                    ('templates/yes_insurance.png', 1),
                    # ('templates/got_it.png', 4),
                    ('templates/agree_terms.png', 3)
                    # ('templates/place_order.png', 2),

                ]
                accept_or_agree_template = ('templates/accept.png', 'templates/agree.png')

                for template, wait_time in templates_to_check:
                    print(template)
                    while True:
                        if template == 'templates/find_tickets.png':
                            time.sleep(5)
                            scroll_pixels = -500

                            while True:
                                pyautogui.scroll(scroll_pixels)
                                time.sleep(2)

                                template_location = pyautogui.locateOnScreen(template)

                                if template_location:
                                    template_x, template_y = pyautogui.center(template_location)
                                    pyautogui.click(template_x, template_y)
                                    break
                            break
                            
                        elif template == 'templates/agree_terms.png':
                            time.sleep(2)
                            scroll_pixels = 1000

                            while True:
                                pyautogui.scroll(scroll_pixels)
                                time.sleep(2)

                                template_location = pyautogui.locateOnScreen(template)

                                if template_location:
                                    template_x, template_y = pyautogui.center(template_location)
                                    pyautogui.click(template_x, template_y)
                                    break
                            break

                        elif template == 'templates/yes_insurance.png':
                            scroll_pixels = -700

                            while True:
                                pyautogui.scroll(scroll_pixels)
                                time.sleep(2)
                                template_location = pyautogui.locateOnScreen(template)

                                if template_location:
                                    template_x, template_y = pyautogui.center(template_location)
                                    pyautogui.click(template_x, template_y)
                                    break
                            break

                        # elif template == 'templates/yes_insurance.png':
                        #     # time.sleep(2)
                        #     scroll_pixels = -2000

                        #     pyautogui.scroll(scroll_pixels)
                        #     time.sleep(2)
                        #     # template_image = 'insurance.png'
                        #     template_location = pyautogui.locateOnScreen(template)

                        #     if template_location:
                        #         template_x, template_y = pyautogui.center(template_location)
                        #         pyautogui.click(template_x, template_y)
                        #     break

                        elif template in accept_or_agree_template:
                            for accept_agree_template in accept_or_agree_template:
                                template_location = pyautogui.locateOnScreen(accept_agree_template)
                                if template_location:
                                    template_x, template_y = pyautogui.center(template_location)
                                    pyautogui.click(template_x, template_y)
                                    break
                            break
                        
                        else:
                            template_location = pyautogui.locateOnScreen(template)
                            print("else", template)
                            # time.sleep(2)

                            if template_location:
                                template_x, template_y = pyautogui.center(template_location)
                                pyautogui.click(template_x, template_y)
                                
                                if template == 'templates/cvv.png':
                                    pyautogui.write(self.cvv)
                                break
                            else:
                                cnt+=1
                                if cnt > 10:
                                    cnt = 0
                                    break
                                time.sleep(wait_time)

        def logout():
            cnt = 0
            pyautogui.hotkey('ctrl', 't')
            time.sleep(2)
            url = "https://www.ticketmaster.com"
            pyautogui.write(url)
            pyautogui.press("enter")

            templates_to_check = [
                ('templates/my_account.png', 6),
                ('templates/sign_out.png',5),
            ]
            for template, wait_time in templates_to_check:
                print(template)
                while True:
                    template_location = pyautogui.locateOnScreen(template)

                    if template_location:
                        template_x, template_y = pyautogui.center(template_location)
                        pyautogui.click(template_x, template_y)
                        break

                    else:
                        cnt+=1
                        if cnt > 10:
                            cnt = 0
                            break
                        time.sleep(wait_time)            
        booking_with_login()
        multiple_booking()
        logout()

    def exit_app(self):
        self.destroy()

if __name__ == "__main__":
    app = TicketingBotApp()
    app.protocol("WM_DELETE_WINDOW", app.exit_app)
    app.mainloop()
