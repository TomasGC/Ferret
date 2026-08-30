package com.ferret.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text

// TODO: replace with real navigation between login, company browser,
// criteria editor, and offers feed screens. See ARCHITECTURE.md "Android app".
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface {
                    Text("Ferret")
                }
            }
        }
    }
}
