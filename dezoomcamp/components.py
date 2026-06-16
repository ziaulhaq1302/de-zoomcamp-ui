import streamlit as st


def craftcourse_banner():
    st.markdown("---")
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #1a1a3d 0%, #212750 100%);
                    border: 1px solid #5681d0; border-radius: 12px; padding: 20px 24px; margin: 8px 0;">
            <p style="font-size: 15px; color: #c9d6f0; margin: 0 0 10px 0;">
                📚 Ever started a course… and never finished it? YouTube rabbit holes, no structure, no accountability.
            </p>
            <p style="font-size: 15px; color: #e8edf8; margin: 0 0 14px 0;">
                <strong>CraftCourse</strong> is an AI learning platform that generates a full structured learning path
                around <em>your</em> goal, level, and schedule — then keeps you accountable until you finish.
                AI tutor, quizzes, flashcards, XP, streaks, certificates, and more.
            </p>
            <a href="https://craftcourse.app" target="_blank"
               style="display: inline-block; background-color: #5681d0; color: white;
                      padding: 8px 20px; border-radius: 8px; text-decoration: none;
                      font-weight: 600; font-size: 14px;">
                🚀 Try CraftCourse free →
            </a>
            <span style="font-size: 12px; color: #8899bb; margin-left: 12px;">Free for the first 1,000 users · Now in beta</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
