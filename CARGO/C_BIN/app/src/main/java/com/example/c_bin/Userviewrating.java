package com.example.c_bin;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RatingBar;
import android.widget.Spinner;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userviewrating extends AppCompatActivity implements JsonResponse{

    RatingBar r1;
    Button b1;
    String rate,comment;
    public static String bids;

    EditText e1;
    Spinner s1;
    String[] branchname,bid,value;
    Float rated;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewrating);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        r1 = (RatingBar) findViewById(R.id.etrate);
        b1=(Button)findViewById(R.id.button);
        e1=(EditText)findViewById(R.id.etcomment);
        // l1=(ListView)findViewById(R.id.lvview);
        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Userviewrating.this;
        String q="/userviewrating?lid="+sh.getString("log_id","")+"&bid="+Userviewnearbycargoservices.bids;
        q=q.replace(" ","%20");
        JR.execute(q);

    }

    @Override
    public void response(JSONObject jo) {

        try {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {

                    rate=jo.getString("data");

                    rated=Float.parseFloat(rate);
                    e1.setText(jo.getString("review"));
                    e1.setEnabled(false);
                    Toast.makeText(getApplicationContext(),rated+"", Toast.LENGTH_SHORT).show();
                    r1.setRating(rated);
                    r1.setEnabled(false);


            }
        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
}