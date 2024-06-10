package com.example.c_bin;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userbookacargo extends AppCompatActivity implements JsonResponse{
    EditText e1,e2,e3,e4,e5;
    Button b1;
    String weight,length,width,fromloaction,tolocation;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userbookacargo);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.weight);
        e2=(EditText)findViewById(R.id.length);
        e3=(EditText)findViewById(R.id.width);
        e4=(EditText)findViewById(R.id.from);
        e5=(EditText)findViewById(R.id.to);
        b1=(Button)findViewById(R.id.button);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                weight=e1.getText().toString();
                length=e2.getText().toString();
                width=e3.getText().toString();
                fromloaction=e4.getText().toString();
                tolocation=e5.getText().toString();
                if(weight.equalsIgnoreCase(""))
                {
                    e1.setError("Enter Weight");
                    e1.setFocusable(true);
                }
              else  if(length.equalsIgnoreCase(""))
                {
                    e2.setError("Enter Length");
                    e2.setFocusable(true);
                }
                else  if(width.equalsIgnoreCase(""))
                {
                    e3.setError("Enter Width");
                    e3.setFocusable(true);
                }
                else  if(fromloaction.equalsIgnoreCase("")|| !fromloaction.matches("[a-zA-Z ]+"))
                {
                    e4.setError("Enter Fromlocation");
                    e4.setFocusable(true);
                }
                else  if(tolocation.equalsIgnoreCase("")|| !tolocation.matches("[a-zA-Z ]+"))
                {
                    e4.setError("Enter Tolocation");
                    e4.setFocusable(true);
                }

                else {

                    JsonReq JR1 = new JsonReq();
                    JR1.json_response = (JsonResponse) Userbookacargo.this;
                    String q1 = "/userbookacargo?lid=" + sh.getString("log_id", "") + "&bid=" + sh.getString("bid", "") + "&pid=" + Usercheckprices.pids + "&weight=" + weight + "&length=" + length + "&width=" + width + "&fromlo=" + fromloaction + "&toloc=" + tolocation;
                    q1 = q1.replace(" ", "%20");
                    JR1.execute(q1);
                }

            }
        });

    }

    @Override
    public void response(JSONObject jo) {
        try {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "BOOKED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getApplicationContext(), Userbookacargo.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }

             if (status.equalsIgnoreCase("nd")) {
                Toast.makeText(getApplicationContext(), "NO DATA", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Userbookacargo.class));

            } else {

                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
            }




        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
}