import os
import streamlit as st

def main():

    st.write("# Welcome to Streamlit! 👋")

    
    #AT:ee3ecc6b6cc257755dfe60af7f82dc98b9fed765
    # download internlm2 to the base_path directory using git tool
    base_path = './internlm2-chat-7b'
    os.system(f'git clone https://Junco:your_git_token@code.openxlab.org.cn/Junco/firstTry.git {base_path}')
    os.system(f'cd {base_path} && git lfs pull')


if __name__ == "__main__":
    main()
