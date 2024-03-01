from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from datetime import datetime
import json
import ast

from conn.mongodb import (
    get_all_files,
    schedule_kyc
)
"""
Handle KYC
Returns:
    _type_: _description_
"""

interviews_bp = Blueprint(
    "interviews", __name__, template_folder="templates", static_folder="static"
)
print(interviews_bp)


@interviews_bp.get("/schedule_interview")
def Interview_schedules():
    """
    signup Screen for user to Register,
    """
    print("rendering")
    return render_template("schedule_interview.html")

import os
@interviews_bp.route("/create_interview", methods=["GET", "POST"])
def create_interview():
    file = request.files["file"]
    file.save(os.path.join("InterviewDocs", file.filename))
    file_path = os.path.join("InterviewDocs", file.filename)

    interview_time = request.form["interviewTime"]
    print("---------", file_path)
    print("-------------", interview_time)
    schedule_kyc(
        kyc_details={
            "file_path": file_path,
            "interviewtime": datetime.strptime(interview_time, "%Y-%m-%dT%H:%M"),
            "meetingurl": "https://meet.google.com/bzr-sjyn-bkq",
        }
    )
    return jsonify({"status": True})
