import streamlit as st

class BaseConverter:
    def __init__(self, number, from_base, to_base):
        self.number = number
        self.from_base = from_base
        self.to_base = to_base
    
    def convert(self):
        # แปลงจาก decimal ไป base ที่ target
        decimal_number = self.to_decimal(self.number, self.from_base) #
        if self.to_base == 10:
            return str(decimal_number)
        else:
            return self.from_decimal(decimal_number, self.to_base)

    @staticmethod
    def to_decimal(number, base):
        """Converts a number from a given base to decimal (base 10)."""
        return int(number, base)

    @staticmethod
    def from_decimal(decimal_number, base):
        """Converts a decimal number (base 10) to a given base."""
        digits = "0123456789ABCDEF"
        if decimal_number < base:
            return digits[decimal_number]
        else:
            return BaseConverter.from_decimal(decimal_number // base, base) + digits[decimal_number % base]

# Display conversions for bases 2 to 10


class Component:
    def __init__(self) -> None:
        self.front_value = 2
        self.last_value = 2
    
    def converter(self, number, from_base, to_base):
        

        # Validate inputs and perform conversion
        if st.button("Convert"):
            if not number:
                st.error("Please enter a number.")
            else:
                try:
                    converter = BaseConverter(number, from_base, to_base)
                    converted_number = converter.convert()
                    st.success(f"{converted_number}")
                except ValueError as e:
                    st.error(f"{number} is not in base {from_base}")
    @staticmethod
    def convertList(base_next):

        def create_clickable_link(text, key):
            url = f"http://localhost:8501/ConvertBase/?convert_from={key}"
            return f"[{text}]({url})"
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Params:")
            links = [create_clickable_link(f"From base {i} to base {base_next}", f"{i}-to-{base_next}") for i in range(2,17) if base_next != i]
            st.markdown("<br>".join(links), unsafe_allow_html=True)

        # Display r_params in column 2
        with col2:
            st.write("R_Params:")
            links = [create_clickable_link(f"From base {base_next} to base {i}", f"{base_next}-to-{i}") for i in range(2,17) if base_next != i]
            st.markdown("<br>".join(links), unsafe_allow_html=True)

    def run(self):
        
        params = st.query_params

        if params:
            front_value = params.get("convert_from")[0] if params.get("convert_from")[1] == "-" else params.get("convert_from")[0:2]
            last_value = params.get("convert_from")[-1] if params.get("convert_from")[-2] == "-" else params.get("convert_from")[-2:]
            self.front_value = int(front_value)
            self.last_value = int(last_value)

            convert_selection = params.get("convert_from", ["No Selection"])
            if convert_selection:
                st.session_state.selected_value = convert_selection

            # st.write("Current selection:", st.session_state.get('selected_value', 'No selection'))
                
            st.title("Base Converter")

            number = st.text_input("Enter the number to convert:", "1010")
            from_base = st.number_input("From base:", min_value=2, max_value=16, value=self.front_value, format="%d")
            to_base = st.number_input("To base:", min_value=2, max_value=16, value=self.last_value, format="%d")

            app.converter(number, from_base, to_base)

            self.convertList(to_base)

        # Populate params and r_params lists
        # Layout with two columns
        if not params:
            to_base = 2
            self.convertList(to_base)

            # Display params in column 1

        # Example usage of query params and session state

        


        
            
        # Update session state based on selection

        # Optionally, display the current selection or session state






        # def create_clickable_link(text, key):
        #     url = f"http://localhost:8501/ConvertBase/?convert_form={key}"
        #     return f"[{text}]({url})"
        
        # base = range(1, 11)  # Generates numbers from 1 to 10

        # params = st.query_params
        # convert_selection = params.get("convert_form", [i for i in self.params])
        # r_convert_selection = params.get("covert_form", [i for i in self.r_params])



        # if convert_selection or r_convert_selection:
        #     st.session_state.selected_value = convert_selection
        #     st.session_state.selected_value = r_convert_selection

        # st.write(st.session_state)

        # links = [create_clickable_link(f"Convert base {i} to base 10", f"{i}-to-10") for i in base]

        # base_params = params.get("convert_form")

        # if st.session_state.get("selected_value") == base_params:
        #      del st.session_state["selected_value"]

        # st.text_input(f"Base {base_params}", placeholder=f"Base {base_params}")

        # st.button("Submit")
        # st.button("Transfer")
        # st.markdown("<br>".join(links), unsafe_allow_html=True)


        # current_selection = st.session_state.get("selected_value", "No selection")
        # st.write(f"Current selection: {current_selection}")
        # st.write(st.query_params)




if __name__ == "__main__":
    st.query_params.get("df", "dsf")
    app = Component()
    app.run()
    
    
    